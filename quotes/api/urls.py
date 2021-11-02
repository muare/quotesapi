from django.urls import path
from quotes.api.views import QuoteListCreateAPIView, QuoteRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('quotes/', QuoteListCreateAPIView.as_view(), name='quote-list'),
    path('quotes/<int:pk>/', QuoteRetrieveUpdateDestroyAPIView.as_view(),
         name='quote-detail'),
]
