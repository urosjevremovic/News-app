from django.contrib.auth.decorators import login_required
from django.urls import path

from articles.views import ArticleList, ArticleUpdate, ArticleDetail, ArticleDelete, ArticleCreate, CommentCreate

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('new/', login_required(ArticleCreate.as_view()), name='article_new'),
    path('<int:pk>/edit/', login_required(ArticleUpdate.as_view()), name='article_edit'),
    path('<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('<int:pk>/comment/', login_required(CommentCreate.as_view()), name='comment_new'),
    path('<int:pk>/delete/', login_required(ArticleDelete.as_view()), name='article_delete'),
]