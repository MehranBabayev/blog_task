from django.db import models
# from apps.core import models as mod_core

# from apps.blog.models import Blog, Blog_comment
from apps.blog import models as mod_blog




class PublishedBlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                    .filter(status=mod_blog.Blog.Status.PUBLISHED)


class PublishedCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                    .filter(status=mod_blog.Blog_comment.Status.PUBLISHED)