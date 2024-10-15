from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import BooksForm, BookCommentForm
from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library:list')
        else:
            return HttpResponse('Form is invalid')

    form = {'form': BooksForm}
    return render(request, 'add_book.html', form)

@login_required
def book_list(request):
    books = Book.objects.all()
    ctx = {'books': books}
    return render(request, 'book_list.html', ctx)

@login_required
def book_detail(request, pk):

    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()

    if request.method == 'POST':
        form = BookCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
            return redirect('library:detail', pk=pk)
        else:
            form_is_invalid = 'Comment is invalid'
            ctx = {'book': book, 'comments': comments, 'form': form, 'invalid': form_is_invalid}
            return render(request, 'book_detail.html', ctx)

    form = BookCommentForm()
    ctx = {'book': book, 'comments': comments, 'form': form}
    return render(request, 'book_detail.html', ctx)

@login_required
def update_book(request, pk):

    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BooksForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('library:detail', pk=pk)
        else:
            return HttpResponse('Form is invalid')

    form = {'form': BooksForm(instance=book), 'book': book}
    return render(request, 'add_book.html', form)

@login_required
def delete_book(request, pk):

    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('library:list')

    return render(request, 'confirm.html', {'book': book})

@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')
