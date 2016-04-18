from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField('Post header:', max_length=100, unique=True)
    text = RichTextField('Post text:')
    text_for_main_page = RichTextField('Post text for the main page:', blank=True)
    pub_date = models.DateTimeField('Publication date:', auto_now=True)
    slug = models.SlugField('URL slug:', unique=True,)  # из этой части будет стоиться URL. Автозаполняется в admin.py

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blogtopic:detail', args=[self.slug],)

# Follow this description for below function description:
# For every DateField and DateTimeField that does not have null=True,
# the object will have get_next_by_FOO() and get_previous_by_FOO() methods,
# where FOO is the name of the field. This returns the next and previous
# object with respect to the date field, raising a DoesNotExist exception when appropriate.
    def get_next_post_title(self):
        try:
            result = self.get_previous_by_pub_date().title
        except Post.DoesNotExist:
            return None
        return result

    def get_previous_post_title(self):
        try:
            result = self.get_next_by_pub_date().title
        except Post.DoesNotExist:
            return None
        return result

    def get_next_post_slug(self):
        try:
            result = self.get_previous_by_pub_date().slug
        except Post.DoesNotExist:
            return None
        return result

    def get_previous_post_slug(self):
        try:
            result = self.get_next_by_pub_date().slug
        except Post.DoesNotExist:
            return None
        return result


class Comment(models.Model):
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_who_created = models.ForeignKey(User, on_delete=models.CASCADE)
    text = RichTextField('Leave your comment here:')
    pub_date = models.DateTimeField('Publication date',)

    def __str__(self):
        return self.text
