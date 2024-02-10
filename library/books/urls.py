from django.urls import path
from . import views


app_name = 'books'
urlpatterns = [
    path('homepage',views.homepage, name = 'homepage'),
    path('books',views.CreateBook ,name ="create-book"),
    path('display',views.BookDisplay,name ='display'),
    path('book-details/<int:pk>/',views.BookDetail, name='book-details'),
    path('search/',views.SearchWord, name='searched-page'),
    path('genres/', views.genre_list, name='genre-list'),
    path('genres/<int:genre_id>/', views.books_by_genre, name='books-by-genre'),
    path('bookshelf/',views.bookshelf, name='bookshelf'),


   # not working- path('view-file/<int:pk>/', views.ReadBook, name='view-file'),
]
