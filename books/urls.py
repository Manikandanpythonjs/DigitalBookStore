from django.urls import path
from . import views


urlpatterns = [

    path('', views.BooksShow.as_view(), name='book.all'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book.show'),
    path('<int:id>/review', views.ReviewBook, name="book.review"),
    path('<str:author>/authorListBook',
         views.AuthorListBook, name="book.authors"),


]
