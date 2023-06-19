from rest_framework import serializers
from url_shortener.models import ShortenedUrl
from rest_framework.reverse import reverse

class OriginalUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedUrl
        fields = ("original_url",)

class ShortenedUrlCreateSerializer(serializers.ModelSerializer):
    shortened_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ShortenedUrl
        fields = ("original_url", "shortened_url")
    
    def get_shortened_url(self, obj) -> str:
        return reverse("get_original_url", args=[obj.hash], request=self.context.get("request"))
