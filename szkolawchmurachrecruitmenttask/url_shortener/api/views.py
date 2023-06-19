from rest_framework import generics
from url_shortener.models import ShortenedUrl
from url_shortener.api.serializers import OriginalUrlSerializer, ShortenedUrlCreateSerializer

class GetOriginalUrlAPIView(generics.RetrieveAPIView):
    """
    This functionality could be handled in two particaular ways:
    1. Retrieve ShortenedUrl instance, simply return original url and let frontend handle redirection
    2. Retrieve ShortenedUrl instance and return HttpResponseRedirect redirecting to original url
    Since this demo is supposed to be as minimalistic as possible I chose to do it the first way.
    """
    lookup_field = "hash"
    queryset = ShortenedUrl.objects.all()
    serializer_class = OriginalUrlSerializer

class CreateShortenedUrlAPIView(generics.CreateAPIView):
    serializer_class = ShortenedUrlCreateSerializer
