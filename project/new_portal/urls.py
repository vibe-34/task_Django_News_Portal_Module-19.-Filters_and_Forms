from django.urls import path
from .views import NewsList, NewsDetail, PostCreate, PostUpdate

urlpatterns = [
	path('', NewsList.as_view(), name='news'),
	path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
	path('create/', PostCreate.as_view(), name='post_create'),
	path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
	]
