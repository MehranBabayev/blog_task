from django.contrib import admin
from apps.blog.models import Blog, Blog_comment, LikeDislike, IPs, Category, Tag
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from apps.blog.utils.filters import DislikedCountFilter, LikedCountFilter, ViewCountListFilter



class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'view_blog_authors_link', 'published_at', 'status', 'comments_count', 'view_count')
    list_filter = ('status', 'published_at', 'categories', 'tags', ViewCountListFilter)
    search_fields = ['blog_title', 'blog_author__username']
    date_hierarchy = 'published_at'
    list_per_page = 20
    actions = ['make_draft', 'make_published']
    readonly_fields = ['slug']
    autocomplete_fields = ['blog_author']
    filter_horizontal = ['categories', 'tags']

    def view_blog_authors_link(self, obj):
        user = obj.blog_author
        url = (
            reverse("admin:blog_blog_changelist")
            + "?"
            + urlencode({"blog_author__id": f"{obj.blog_author.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, user)

    view_blog_authors_link.short_description = "blog_author"

    def comments_count(self, obj):
        return obj.blog_comments.count()

    comments_count.short_description = 'Comments Count'

    def make_draft(modeladmin, request, queryset):
        queryset.update(status='DF')
    make_draft.short_description = "Set selected blogs to Draft"

    def make_published(modeladmin, request, queryset):
        queryset.update(status='PB')
    make_published.short_description = "Set selected blogs to Published"

    actions = [make_draft, make_published]


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ('truncated_comment_text', 'comment_author', 'view_blogs_link', 'published_at', 'active', 'like_count', 'dislike_count',)
    list_filter = ('active', 'published_at', LikedCountFilter, DislikedCountFilter)
    search_fields = ['blog', 'comment_author__username']
    date_hierarchy = 'published_at'
    list_per_page = 20
    actions = ['make_inactive', 'make_active']
    readonly_fields = ['slug']
    autocomplete_fields = ['blog']

    def view_blogs_link(self, obj):
        blogs = obj.blog
        url = (
            reverse("admin:blog_blog_comment_changelist")
            + "?"
            + urlencode({"blog__id": f"{obj.blog.id}"})
        )
        return format_html('<a href="{}">{}</a>', url, blogs)

    view_blogs_link.short_description = "blog"

    def make_active(modeladmin, request, queryset):
        queryset.update(active=True)

    make_active.short_description = "Set selected blogs to Active"

    def make_inactive(modeladmin, request, queryset):
        queryset.update(active=False)

    make_inactive.short_description = "Set selected blogs to Inactive"

    def truncated_comment_text(self, obj):
        return obj.comment_text[:25] + "..." if len(obj.comment_text) > 25 else obj.comment_text

admin.site.register(Blog, BlogAdmin)
admin.site.register(Blog_comment, BlogCommentAdmin)

@admin.register(LikeDislike)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'action')

@admin.register(IPs)
class IPsAdmin(admin.ModelAdmin):
    list_per_page = 20
    readonly_fields = ('view_ip', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ['name']