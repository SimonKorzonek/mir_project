from django.urls import path
from .views import ArticleDetailView, ArticleListView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('article-detail/<int:pk>/<slug:slug>', ArticleDetailView.as_view(), name='article-detail'),
]
