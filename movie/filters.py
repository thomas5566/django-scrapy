from django import forms
from .models import Movie
import django_filters

class MovieFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(
        lookup_expr='icontains', # lookup_expr(查詢表示式), 模糊查詢=icontains, 完全符合=iexact
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )

    date = django_filters.CharFilter(
        widget = forms.NumberInput(attrs={'class': 'form-control'})
    )

    amount_reviews = django_filters.CharFilter(
        widget = forms.NumberInput(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Movie
        fields = ['title', 'date']