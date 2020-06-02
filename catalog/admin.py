from django.contrib import admin
from .models import Category, Publication, Book, Review, Author, BookRequestModel

#Admin cutomization

admin.site.site_title = 'TechBooks'
admin.site.site_header = 'TechBooks'
admin.site.index_title = 'Admin Dashboard'

# Register your models here for Admin dashboard.
admin.site.register(Category)
admin.site.register(Publication)

class BookItemsInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    inlines = [BookItemsInline]
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication', 'category')

admin.site.register(BookRequestModel)
admin.site.register(Review)