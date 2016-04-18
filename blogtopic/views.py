from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Post, Comment
from .forms import CommentForm


class PostListView(generic.ListView):
    model = Post
    template_name = 'blogtopic/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('pub_date')


def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comment_list_sorted_date = post.comment_set.all().order_by('pub_date')
    user = None
    if request.user.is_authenticated():
            user = request.user
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(user_who_created=user,
                                  related_post=post,
                                  text=form.cleaned_data['text'],
                                  pub_date=timezone.now())
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'blogtopic/detail.html',
                  {'post': post,
                   'form': form,
                   'user': user,
                   'comment_list': comment_list_sorted_date,
                   'error_message_comment': "Requested Post does not exist", })


def comment_edit_view(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.related_post
    comment_list_sorted_date = post.comment_set.all().order_by('pub_date')
    user = None
    if request.user.is_authenticated():
        user = request.user
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.text = form.cleaned_data['text']
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    return render(request, 'blogtopic/detail.html',
                  {'post': post,
                   'form': form,
                   'user': user,
                   'comment_list': comment_list_sorted_date,
                   'error_message_comment': "Requested Comment does not exist", })


class CommentDeleteView(generic.DeleteView):
    model = Comment

    def get_object(self, queryset=None):
        obj = super(CommentDeleteView, self).get_object()
        if not obj.user_who_created == self.request.user:
            raise Http404
        return obj

    def get_success_url(self):
        related_post_slug = self.get_object().related_post.slug
        return reverse('blogtopic:detail', args=[related_post_slug], )
