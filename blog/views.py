from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Article


class ArticleListView(ListView):
    model = Article
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)
        return queryset


class ArticleDetail(DetailView):
    model = Article

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.views_count_ink()
        obj.save()
        if obj.views_count == 100:
            send_mail(
                "Поздравляю!",
                f"Ура! Статья '{obj.heading}' набрала {obj.views_count} просмотров.",
                "uv.rogova@yandex.ru",
                ["aelitadi@yandex.ru"],
                fail_silently=False,
            )
        return obj


class ArticleCreateView(CreateView):
    model = Article
    fields = ('heading', 'content', 'image', 'is_published',)
    success_url = reverse_lazy('blog:article_list')


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    fields = ['heading', 'content', 'image', 'is_published']
    permission_required = 'blog.change_article'

    def get_success_url(self):
        return reverse_lazy('blog:article_detail', args=[self.kwargs.get('pk')])


class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article_list')
    permission_required = 'blog.delete_article'
