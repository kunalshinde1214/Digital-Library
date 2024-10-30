from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm


@login_required
def book_list(request):
    books = Book.objects.all()

    # Filter by genre
    genre = request.GET.get('genre')
    if genre:
        books = books.filter(genre=genre)

    # Filter by language
    language = request.GET.get('language')
    if language:
        books = books.filter(language=language)

    context = {
        'books': books,
        'book_genres': Book.GENRE_CHOICES,
        'book_languages': Book.LANGUAGE_CHOICES,
        'selected_genre': genre,
        'selected_language': language,
    }
    return render(request, 'library/book_list.html', context)
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" was successfully added!')
            return redirect('library:book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form, 'title': 'Add New Book'})

@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" was successfully updated!')
            return redirect('library:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form, 'title': 'Edit Book'})