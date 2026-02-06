from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Book
from .forms import BookForm

class BookListView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(author__icontains=q) |
                Q(journal__icontains=q) |
                Q(publisher__icontains=q)
            )
        return queryset

class BookDetailView(DetailView):
    model = Book
    template_name = 'details.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'create.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'update.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = reverse_lazy('book_list')
