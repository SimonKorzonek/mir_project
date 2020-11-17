from django.views.generic import DetailView, ListView
from .models import Article

class ArticleListView(ListView):
    model = Article
    paginate_by = 5

    def get_context_data(self, object_list=None):
        queryset = object_list if object_list is not None else self.object_list
        queryset = queryset.filter(online=True)
        return super().get_context_data(object_list=queryset)


class ArticleDetailView(DetailView):
    model = Article
