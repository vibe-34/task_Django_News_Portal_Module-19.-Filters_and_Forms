from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-time_in'  # сортировка по времени создания (от более свежей публикации)
    template_name = 'news.html'  # шаблон с инструкциями об отражении страницы
    context_object_name = 'news'  # имя списка содержащего все объекты


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'news_id'
