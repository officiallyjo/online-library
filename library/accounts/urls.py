from django.urls import path
from . import views


app_name ='accounts'
urlpatterns = [
    path('register',views.registration ,name ="register"),
    path('login',views.LoginView ,name ='login'),
    path('logout', views.LogoutView ,name ='logout')

]
