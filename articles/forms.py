from django.forms import ModelForm

from articles.models import Comment


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]