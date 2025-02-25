from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the genre (e.g., Rock, Pop)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'