from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from apps.blog.utils.manager import PublishedBlogManager, PublishedCommentManager
from apps.users.models import CustomUser


class IPs(models.Model):
    view_ip = models.GenericIPAddressField('IP ünvanı', editable=False, null=True)

    class Meta:
        verbose_name = ('IP ünvanı')
        verbose_name_plural = ('IP ünvanları')

    def __str__(self) -> str:
        return str(self.view_ip)



class Category(models.Model):
    name = models.CharField('Kateqoriya adı', max_length=100, unique=True)
    slug = models.SlugField('Link adı', unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField('Teq adı', max_length=100, unique=True)
    slug = models.SlugField('Link adı', unique=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Teq'
        verbose_name_plural = 'Teqlər'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Base(models.Model):
    
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    created_at = models.DateTimeField('Əlavə edilmə tarixi', auto_now_add=True) 
    updated_at = models.DateTimeField('Yenilənmə tarixi',auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    published_at = models.DateTimeField('Nəşr tarixi',default=timezone.now)
    
    class Meta:
        abstract=True
            
    @property
    def published_date(self):
        return self.published_at.strftime('%d.%m.%Y')

                
class Blog(Base):
    blog_title = models.CharField('Blogun başlığı', max_length=150, unique=True)
    blog_content = RichTextField('Blogun mətni', null=True)
    blog_image = models.ImageField('Blogun fotosu', upload_to="blog/", unique=True)
    slug = models.SlugField('Link adı', help_text="Bu qismi boş buraxın. Avtomatik doldurulacaq.", max_length=250, null=True, blank=True)
    blog_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blogs', null=True)
    viewed_ips = models.ManyToManyField(IPs, related_name="blogs", verbose_name='Blogların görüntüləndiyi IP ünvanları', editable=False)
    categories = models.ManyToManyField(Category, related_name='blogs', verbose_name='Kateqoriyalar')
    tags = models.ManyToManyField(Tag, related_name='blogs', verbose_name='Teqlər')
    objects = models.Manager()
    published = PublishedBlogManager()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at']),
        ]

    def __str__(self):
        return self.blog_title

    @property
    def view_count(self):
        return self.viewed_ips.count() if self.viewed_ips else 0

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title)
        super().save(*args, **kwargs)

    @property
    def published_blog_count(self):
        return Blog.published.count()

    @property
    def blog_user(self):
        return f'{self.blog_author.first_name} {self.blog_author.last_name}'

                
class Blog_comment(Base):
    comment_text =models.TextField('Bloga rəylər')
    comment_author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='blog_comment', null=True, blank=True)
    slug = models.SlugField('Link adı',help_text="Bu qismi boş buraxın. Avtomatik doldurulacaq.", max_length=250, null=True, blank=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='blog_comments', null=True, blank=True)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    published = PublishedCommentManager()

    class Meta:
        verbose_name = "Bloga rəy"
        verbose_name_plural = "Bloga rəylər"
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at']),
        ]
        
    def __str__(self):
        return self.comment_text[:50] + "..." if len(self.comment_text) > 50 else self.comment_text

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.comment_text)
        if self.active:
            self.status = self.Status.PUBLISHED
        else:
            self.status = self.Status.DRAFT
        super().save(*args, **kwargs)
        

    
    @property
    def like_count(self):
        return LikeDislike.objects.filter(comment=self, action=LikeDislike.LIKE).count()

    @property
    def dislike_count(self):
        return LikeDislike.objects.filter(comment=self, action=LikeDislike.DISLIKE).count()
    

class LikeDislike(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    ACTION_CHOICES = [
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.ForeignKey(Blog_comment, on_delete=models.CASCADE)
    action = models.CharField(max_length=7, choices=ACTION_CHOICES)
