# imports
from django.db import models
from django.urls import reverse


#Model for Category
class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter book category')
    icon = models.FileField('SVG File',upload_to='icons/', blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])
        
    def __str__(self):
        return self.name

#Model for Author
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        ordering =['first_name', 'last_name']

    """String for representing the Model object."""
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#Model for Publication
class Publication(models.Model):
    name = models.CharField(max_length=200, help_text='Enter book publication')

    """String for representing the Model object."""
    def __str__(self):
        return f'{self.name}'

# Model for Books
class Book(models.Model):
    title = models.CharField(max_length=200, help_text = 'Book title')
    isbn = models.CharField('ISBN', unique=True, blank = True, max_length = 13, help_text = '13 Character <a target="_blank" href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null=True)
    publication = models.ForeignKey('Publication', on_delete = models.SET_NULL, null=True)
    published = models.DateField('Published on', auto_now=False, auto_now_add=False, help_text = 'Publication date')
    category = models.ForeignKey('Category', on_delete = models.SET_NULL, null=True)
    image = models.ImageField('Cover Image',upload_to='images/', blank=True)
    pdffile = models.FileField('PDF File',upload_to='files/', blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

#Model for Reviews
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    book_linked = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ['posted_on']
        unique_together = ('email', 'book_linked')

    def __str__(self):
        return 'Comment on {} by {}'.format(self.book_linked, self.name)

#Model for Book Requests
class BookRequestModel(models.Model):
    User_Name = models.CharField(max_length=100)
    User_Email = models.EmailField(primary_key=True)
    Book_Title = models.CharField(max_length=200)
    Book_Author = models.CharField(max_length=100)
    Book_ISBN = models.IntegerField()

    class Meta:
        verbose_name_plural = "Book Request"
        
    def __str__(self):
        return self.Book_Title
