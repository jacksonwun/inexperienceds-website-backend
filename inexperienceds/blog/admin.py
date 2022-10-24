from django.contrib import admin
from .models import Author, Tag, Language, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('language',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
