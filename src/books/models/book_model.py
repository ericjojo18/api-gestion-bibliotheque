from django.db import models


class BookModel(models.Model):
    title = models.CharField(max_length=255) # title pour le titre du livre
    author = models.CharField(max_length=255) # author pour le nom  de l'auteur du livre
    quantity = models.IntegerField(default=0) # quantity pour le nombre de livre disponible pour cette oeuvre
    publication_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True) # pour la disponibilie du livre

    def __str__(self):
        return f"{self.title}"
