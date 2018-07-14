from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.core.exceptions import PermissionDenied

from articles.models import Article


class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetail(DetailView, LoginRequiredMixin):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleCreate(CreateView, LoginRequiredMixin):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'body', ]
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdate(UpdateView, LoginRequiredMixin):
    model = Article
    fields = ['title', 'body']
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user
        if user.is_staff or user.is_superuser:
            Article.objects.get(pk=pk)
            return super().dispatch(request, *args, **kwargs)
        try:
            Article.objects.get(pk=pk, author=user)
            return super().dispatch(request, *args, **kwargs)
        except Article.DoesNotExist:
            raise PermissionDenied


class ArticleDelete(DeleteView, LoginRequiredMixin):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user
        if user.is_staff or user.is_superuser:
            Article.objects.get(pk=pk)
            return super().dispatch(request, *args, **kwargs)
        try:
            Article.objects.get(pk=pk, author=user)
            return super().dispatch(request, *args, **kwargs)
        except Article.DoesNotExist:
            raise PermissionDenied
