from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import PostForm
from .models import Post, Author
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = '-time_in'  # сортировка по времени создания (от более свежей публикации)
    template_name = 'news.html'  # шаблон с инструкциями об отражении страницы
    context_object_name = 'news'  # имя списка содержащего все объекты
    paginate_by = 10  # указываем количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации. self.request.GET содержит объект QueryDict
        # сохраняем нашу фильтрацию в объекте класса, чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs  # Возвращаем из функции отфильтрованный список товаров

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'news_id'


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('news')  # URL для перенаправления после успешного создания поста

    def form_valid(self, form):
        author = Author.objects.get(user=self.request.user)
        form.instance.author = author  # Устанавливаем автора
        return super().form_valid(form)
