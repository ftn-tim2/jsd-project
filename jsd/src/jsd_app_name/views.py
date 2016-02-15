from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from jsd_app_name.models import Book
from jsd_app_name.models import Picture
from jsd_app_name.models import Film


class BookList(ListView):
    model = Book


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('jsd_app_name:book_list')


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author']
    success_url = reverse_lazy('jsd_app_name:book_list')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('jsd_app_name:book_list')


class PictureList(ListView):
    model = Picture


class PictureCreate(CreateView):
    model = Picture
    fields = ['name', 'fake']
    success_url = reverse_lazy('jsd_app_name:picture_list')


class PictureUpdate(UpdateView):
    model = Picture
    fields = ['name', 'fake']
    success_url = reverse_lazy('jsd_app_name:picture_list')


class PictureDelete(DeleteView):
    model = Picture
    success_url = reverse_lazy('jsd_app_name:picture_list')


class FilmList(ListView):
    model = Film


class FilmCreate(CreateView):
    model = Film
    fields = ['title', 'author', 'book', 'duration']
    success_url = reverse_lazy('jsd_app_name:film_list')


class FilmUpdate(UpdateView):
    model = Film
    fields = ['title', 'author', 'book', 'duration']
    success_url = reverse_lazy('jsd_app_name:film_list')


class FilmDelete(DeleteView):
    model = Film
    success_url = reverse_lazy('jsd_app_name:film_list')
