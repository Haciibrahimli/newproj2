from django.contrib import admin
from my_app.models import Category
from my_app.models import Author
from my_app.models import Keywords
from my_app.models import Book

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Keywords)
admin.site.register(Book)

