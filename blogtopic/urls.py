from django.conf.urls import url

from . import views

app_name = 'blogtopic'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='index'),
    url(r'delete-comment/(?P<pk>[0-9]+)/$', views.CommentDeleteView.as_view(), name='delete_comment'),
    url(r'edit-comment/(?P<pk>[0-9]+)/$', views.comment_edit_view, name='edit_comment'),
    url(r'(?P<slug>.+)/$', views.post_detail_view, name='detail'),
]