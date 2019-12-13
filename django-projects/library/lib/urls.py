from django.urls import path
from .import views
urlpatterns = [
path('first/',views.intro,name='intro'),
path('add/',views.add_books,name='add_books'),
path('view/<int:book_id>',views.view_books,name='view_books'),
path('edit/<int:book_id>',views.edit_books,name='edit_books'),
path('delete/<int:book_id>',views.delete_books,name='delete_books')
]