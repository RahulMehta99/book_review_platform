from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review
from django.db.models import Q

def book_list(request):
    query = request.GET.get('search', '')
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__icontains=query)
        )
    else:
        books = Book.objects.all()
    return render(request, 'reviews/book_list.html', {'books': books})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Review

def book_detail(request, book_id):
    # Fetch the book and its reviews
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book)
    
    # Generate a range for rating options (1 to 5)
    ratings = range(1, 6)  
    
    # Render the template with book, reviews, and ratings context
    return render(request, 'reviews/book_detail.html', {
        'book': book,
        'reviews': reviews,
        'ratings': ratings,
    })

def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        Book.objects.create(
            title=title, author=author, genre=genre,
            description=description, published_date=published_date
        )
        return redirect('book_list')
    return render(request, 'reviews/book_form.html')

def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')
