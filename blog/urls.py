from django.urls import path
from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetail, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('article/list/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name='article_update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/create/', ArticleCreateView.as_view(), name='article_create'),
]
