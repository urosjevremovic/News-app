from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from articles.models import Article


class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdate(UpdateView, LoginRequiredMixin):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user
        if user.is_staff:
            Article.objects.get(pk=pk)
        try:
            Article.objects.get(pk=pk, user=user)
            return super().dispatch(request, *args, **kwargs)
        except Article.DoesNotExist:
            return HttpResponseForbidden()


class ArticleDelete(DeleteView, LoginRequiredMixin):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user
        if user.is_staff:
            Article.objects.get(pk=pk)
        try:
            Article.objects.get(pk=pk, user=user)
            return super().dispatch(request, *args, **kwargs)
        except Article.DoesNotExist:
            return HttpResponseForbidden()