from django.urls import path
from . import views

urlpatterns = [
    path('',views.CategoryListView.as_view(), name='category'),
    path('<int:pk>',views.CategoryBookListView.as_view(), name='category-detail'),
    path('books/',views.BookListView.as_view(), name="books"),
    path('books/<int:pk>', views.bookdetailview, name='book-detail'),
    path('book-search/', views.search, name='book-search-list-view'),
    path('book-request/',views.BookRequestView.as_view(), name='book-request'),
    path('book-request/success/',views.requestSuccess),
    path('book-review', views.reviewformview, name='review-form'),
    path('review-success/',views.reviewSuccess),
] 
