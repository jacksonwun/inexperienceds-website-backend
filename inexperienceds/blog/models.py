from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=32, default="Anonymous")
    about = models.CharField(max_length=256, null=True, blank=True)
    profile_pic = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.author_name

class Tag(models.Model):
    tag = models.CharField(max_length=64)

    def __str__(self):
        return self.tag

class Language(models.Model):
    language = models.CharField(max_length=64)

    def __str__(self):
        return self.language

class Article_manager(models.Manager):
    def get_message():
        pass

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='article_author')
    title = models.CharField(max_length=63)
    caption = models.CharField(max_length=127)
    language = models.ManyToManyField(Language, blank=True, related_name='article_languages')
    content = RichTextField()
    thumbnail = models.URLField(max_length=200, blank=True, null=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='article_tags')

    objects = Article_manager() 