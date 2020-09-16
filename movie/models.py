from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField('title', max_length=255)
    critics_consensus = models.TextField('Consensus')
    date = models.DateField('date', auto_now=False, auto_now_add=False, blank=True)
    poster = models.ImageField('Poster', upload_to="movie/images/")
    amount_reviews = models.PositiveIntegerField('Amount_reviews')
    approval_percentage  = models.PositiveIntegerField('Percentage')


