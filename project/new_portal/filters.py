from django import forms
from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post


class PostFilter(FilterSet):
    author = CharFilter(field_name='author__user__username', label='Author', lookup_expr='iexact')
    title = CharFilter(field_name='title', label='Title', lookup_expr='iregex')  # icontains не работает без учета регистра именно в SQLite
    # time_in = DateFilter(field_name='time_in', widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
    #                      label='Date of publication', lookup_expr='gt')
    time_in = DateFilter(
        field_name='time_in',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата публикации',
        lookup_expr='date__gte',
    )

    class Meta:
        model = Post
        fields = ['author', 'title', 'time_in']
