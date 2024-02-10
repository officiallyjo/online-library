from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
def registration(request):
    form = RegistrationForm()
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.info(request,user +" you have successfully created an account")
            return redirect('accounts:login')
    return render(request,'accounts/register.html',{"form":form})
            
            
def LoginView(request):
    if request.method == "POST": 
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request,"login sucessful")
                return redirect('books:display')
    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})



def LogoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login') 
    return render(request, 'accounts/logout.html')


        