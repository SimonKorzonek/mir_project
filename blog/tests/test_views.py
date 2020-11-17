from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Article

class TestViews(TestCase):
    def setUp(self):
        Article.objects.create(pk=1, title='slug')

    def test_article_list(self):
        response = self.client.get(reverse('article-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_list.html')

    def test_article_detail(self):
        response = self.client.get(reverse('article-detail', kwargs={'pk':1, 'slug':'slug'}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/article_detail.html')