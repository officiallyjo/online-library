from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import BookForm,AddBookForm
from .models import Book,Genre,BookShelf
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def homepage(request):
        # Order by downloads in descending order and get the first five
   # top_five_books = Book.objects.all().order_by[:5]
    return render (request, 'books/homepage.html')


"""@login_required
def CreateBook(request):
    uploads =BookForm()
    if request.method == "POST":
        uploads = BookForm(request.POST,request.FILES)
        if uploads.is_valid():
            uploads.save()
            return redirect("books:display")
    return render (request ,'books/upload_book.html',{"form":uploads})"""

@login_required
def CreateBook(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()  # Call the save method
            return redirect("books:display")

    return render(request, 'books/upload_book.html', {"form": form})

   

@login_required
def BookDisplay(request):
    bookshelf = Book.objects.all().order_by("-time_posted")
    # Number of books to display per page
    books_per_page = 12

    # Create a Paginator instance
    paginator = Paginator(bookshelf, books_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the Page object for the requested page
        current_books = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        current_books = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        current_books = paginator.page(paginator.num_pages)

    return render(request, 'books/display.html', {'books': current_books})

""" #def display_books(request)
#all_books = Book.objects.all()

    # Number of books per page
    books_per_page = 3

    paginator = Paginator(bookshelf, books_per_page)
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page.
        books = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., 9999), deliver the last page.
        books = paginator.page(paginator.num_pages)

   # return render(request, 'books/display.html', {'books': books})
    return render(request, 'books/display.html', {"books": bookshelf})"""




@login_required
def BookDetail(request,pk):
    book = get_object_or_404(Book,pk=pk)
    shelf, created = BookShelf.objects.get_or_create(user=request.user)

    if request.method == 'POST' and 'add_to_shelf' in request.POST:
        shelf.books.add(book)
    return render (request, 'books/book_details.html',{"book":book ,'shelf': shelf})


"""def ReadBook(request, pk):
    try:
        book = Book.objects.get(id=pk)
        with open(book.book.path, 'r') as file:
            content = file.read()
    except Book.DoesNotExist:
        # Handle the case where the book is not found
        content = "Book not found."
    except FileNotFoundError:
        # Handle the case where the file is not found
        content = "File not found"

    return render(request, 'books/read_book.html', {'content': content, 'book': book})"""

def SearchWord(request):
    searched = request.GET.get('q', '')  # Get the value of the 'q' parameter from the URL

    if searched:
        # Use filter() to filter the queryset based on the search term
        searched_books = Book.objects.filter(title__icontains=searched)
    else:
        searched_books = []  # Set to an empty list if there is no search term

    return render(request, 'books/searched_book.html', {
        "searched": searched, 
        "searched_books": searched_books
    })

def genre_list(request):
    genres = Genre.objects.all().order_by('name')
    return render(request, 'books/genre_list.html', {'genres': genres})

def books_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    books = Book.objects.filter(genre=genre)
    return render(request, 'books/books_by_genre.html', {'genre': genre, 'books': books})

def bookshelf(request):
    if request.user.is_authenticated:
        shelf, created = BookShelf.objects.get_or_create(user=request.user)
        books = shelf.books.all()
        return render(request, 'books/bookshelf.html', {'books': books})
    else:
        return redirect('login')  # Redirect to your login view

