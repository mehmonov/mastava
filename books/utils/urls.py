from django.urls import path
from ..views import BookMain ,  BookChange, BookSearch, BookDetailView, BookExchange

urlpatterns = [
    path('', BookMain.as_view()),
    path('change', BookChange.as_view()),
    path('search/',BookSearch.as_view(), name='searchbook'),
    path('detail/<slug:slug>',BookDetailView.as_view(), name='bookdetail' ),
    path('exchange/<int:pk>',BookExchange.as_view(), name="bookexchange"),
    # path('addbook/',)
]
