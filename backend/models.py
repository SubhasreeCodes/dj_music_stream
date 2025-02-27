from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the genre (e.g., Rock, Pop)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the music streaming service
    description = models.TextField(null=True, blank=True)  # A description about the brand
    image_path = models.ImageField(upload_to="brand", default="no_image_available.png")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

