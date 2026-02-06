from django.urls import path

from .views import BookListView
from .views import BookDetailView
from .views import BookCreateView
from .views import BookUpdateView
from .views import BookDeleteView

urlpatterns = [
    path('list/',
         BookListView.as_view(),
         name='book_list'),

    path('create/',
         BookCreateView.as_view(),
         name='book_create'),

    path('details/<int:pk>/',
         BookDetailView.as_view(),
         name='book_detail'),

    path('update/<int:pk>/',
         BookUpdateView.as_view(),
         name='book_update'),

    path('delete/<int:pk>/',
         BookDeleteView.as_view(),
         name='book_delete'),
]
