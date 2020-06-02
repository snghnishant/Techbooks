from catalog.models import Book, Category, Review
from django.views import generic
from django.shortcuts import render, get_object_or_404
from catalog.forms import BookRequestForm, ReviewForm
from django.http import HttpResponseRedirect

#Request Ebook Form View
class BookRequestView(generic.TemplateView):
    template_name = 'request_form.html'

    def get(self, request):
        form = BookRequestForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self,request):
        form = BookRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success/')
        return render(request,self.template_name, {'form':form})

#Request form success View
def requestSuccess(request):
    return render(request, 'request_success.html')


#Review form View
def reviewformview(request):
    template_name = "review-form.html"
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return HttpResponseRedirect('review-success/')
    else:
        review_form = ReviewForm()
    return render(request, template_name,{'review_form': review_form})

#Review form success View
def reviewSuccess(request):
    return render(request, 'review_success.html')

#Categories List View
class CategoryListView(generic.ListView):
    model = Category
    context_object_name = 'category_list'
    queryset = Category.objects.all()
    template_name = 'category.html'

#Category wise book list View
class CategoryBookListView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'cat_book_list.html'

#Book List View
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'  
    queryset = Book.objects.all()
    template_name = 'book_list.html'
 
 #Book detail View
def bookdetailview(request, pk):
    template_name = 'book_detail.html'
    book = get_object_or_404(Book, pk=pk)
    book_id = book.id
    reviews = Review.objects.filter(book_linked= book_id)
    return render(request, template_name, {
        'book': book,
        'reviews': reviews,
    })

#Book search View
def search(request):
    template_name = 'search-result.html'
    query = request.GET.get('q', '')
    if query:
        results = Book.objects.filter(title__icontains=query)
    else:
        results = []
    return render(request, template_name, {'results': results})

