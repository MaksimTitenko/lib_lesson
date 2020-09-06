from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from catalog.models import *


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()
        num_instances_available = BookInstance.objects.filter(status='a').count()
        num_authors = Author.objects.all().count()
        num_visits = request.session.get('num_visits', 1)
        request.session['num_visits'] = num_visits + 1
        context.update({
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_visits': num_visits
        })

        return render(request, self.template_name, context)

class BookListView(ListView):
    model = Book
    paginate_by = 2

class BookDetailView(DetailView):
    model = Book