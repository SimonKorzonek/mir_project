from django.test import SimpleTestCase
from django.urls import resolve, reverse
from blog.views import ArticleListView, ArticleDetailView

class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('article-list')
        self.assertEquals(resolve(url).func.view_class, ArticleListView)

    def test_detail_url_is_resolved(self):
        url = reverse('article-detail', kwargs={'pk':1, 'slug':'slug'})
        self.assertEquals(resolve(url).func.view_class, ArticleDetailView)