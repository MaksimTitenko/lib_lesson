from django.urls import path

from catalog.views import IndexView, BookListView, BookDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail')

]