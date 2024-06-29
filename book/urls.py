from django.urls import path
from book.views import home, login, register, books

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('books/', books, name='books'),
]
