from django.test import TestCase
from blog.models import Article

class TestModel(TestCase):
    def setUp(self):
        self.article1 = Article.objects.create(title = 'title 1 2', content='content')

    def test_slugify(self):
        self.assertEquals(self.article1.slug, 'title-1-2')