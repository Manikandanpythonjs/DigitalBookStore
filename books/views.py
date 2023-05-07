from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
import json
from books.models import Book, Review
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class BooksShow(ListView):

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = context['book'].review_set.order_by("-created_at")
        context["authors"] = context['book'].AuthorName.all()

        return context


# def showBook(request, id):

#     BookDataUnique = get_object_or_404(Book, pk=id)

#     review = Review.objects.filter(bood_id=id).order_by('-created_at')

#     context = {'book': BookDataUnique, 'reviews': review}
#     return render(request, 'books/showBook.html', context)


def AuthorListBook(request, author):

    books = Book.objects.filter(AuthorName__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)


def ReviewBook(request, id):
    if request.user.is_authenticated:

        review = request.POST['commentReview']
        BookDataUnique = get_object_or_404(Book, pk=id)
        refid = BookDataUnique.BookReferenceId
        ReviewData = Review(ReviewComment=review, book_id=id,
                            book_ref=refid, user=request.user)
        ReviewData.save()

    return redirect('/book')
