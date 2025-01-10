from django_filters import FilterSet, CharFilter, DateTimeFilter
from .models import Post


class PostFilter(FilterSet):
    author = CharFilter(field_name='author__user__username', lookup_expr='iexact')
    title = CharFilter(field_name='title', lookup_expr='icontains')
    time_in = DateTimeFilter(field_name='time_in', lookup_expr='gt')

    class Meta:
        model = Post
        fields = ['author', 'title', 'time_in']
