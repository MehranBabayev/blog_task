# Generated by Django 5.0.6 on 2024-06-30 09:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog_comment',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blog.blog'),
        ),
        migrations.AddField(
            model_name='blog_comment',
            name='comment_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(related_name='blogs', to='blog.category', verbose_name='Kateqoriyalar'),
        ),
        migrations.AddField(
            model_name='blog',
            name='viewed_ips',
            field=models.ManyToManyField(editable=False, related_name='blogs', to='blog.ips', verbose_name='Blogların görüntüləndiyi IP ünvanları'),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog_comment'),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='blogs', to='blog.tag', verbose_name='Teqlər'),
        ),
        migrations.AddIndex(
            model_name='blog_comment',
            index=models.Index(fields=['-published_at'], name='blog_blog_c_publish_122f0b_idx'),
        ),
        migrations.AddIndex(
            model_name='blog',
            index=models.Index(fields=['-published_at'], name='blog_blog_publish_fd0506_idx'),
        ),
    ]
