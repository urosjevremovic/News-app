from django.urls import path

from articles.views import ArticleList, ArticleUpdate, ArticleDetail, ArticleDelete, ArticleCreate, CommentCreate

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('new/', ArticleCreate.as_view(), name='article_new'),
    path('<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/comment/', CommentCreate.as_view(), name='comment_new'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]