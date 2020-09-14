from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField('title', max_length=255)
    critics_consensus = models.TextField('Consensus', blank=True, null=True)
    average_grade = models.DecimalField('Average', max_digits=3, decimal_places=2, blank=True, null=True)
    poster = models.ImageField('Poster', blank=True, null=True)
    amount_reviews = models.PositiveIntegerField('Amount_reviews', blank=True, null=True)
    approval_percentage  = models.PositiveIntegerField('Percentage', blank=True, null=True)


