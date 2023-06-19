from django.db import models
from nanoid import generate

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+"
HASH_SIZE = 8  # same as tinyurl

def generate_hash():
    return generate(alphabet=ALPHABET, size=HASH_SIZE)

# Create your models here.

class ShortenedUrl(models.Model):
    original_url = models.TextField()
    hash = models.CharField(max_length=8, default=generate_hash)