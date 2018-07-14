from django.urls import path

from articles.views import ArticleList, ArticleUpdate, ArticleDetail, ArticleDelete

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]