from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    critics_consensus = models.TextField(blank=True, null=True)
    average_grade = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    poster = models.ImageField(blank=True, null=True)
    amount_reviews = models.PositiveIntegerField(blank=True, null=True)
    approval_percentage  = models.PositiveIntegerField(blank=True, null=True)


