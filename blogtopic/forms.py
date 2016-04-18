from django import forms

#from ckeditor.widgets import CKEditorWidget

from .models import Post, Comment


class CommentForm(forms.ModelForm):
    #comment = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Comment
        exclude = ['pub_date', 'related_post', 'user_who_created']



