from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from quotes.models import Quote
from quotes.api.serializers import QuoteSerializer
from quotes.api.permissions import IsAdminUserOrReadOnly

class QuoteListCreateAPIView(ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer     
    permission_classes = [IsAdminUserOrReadOnly]

class QuoteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    