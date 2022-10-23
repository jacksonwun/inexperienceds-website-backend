from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Author, Tag, Language, Article

class LanguageSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        return obj.language

    class Meta:
        model = Language
        fields =['language',]

class TagSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        return obj.tag

    class Meta:
        model = Tag
        fields =['tag',]

class AuthorSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        return obj.author_name

    class Meta:
        model = Author
        fields =['author_name',]

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    language = LanguageSerializer(read_only=True, many=True)
    class Meta:
        model = Article
        fields = ('__all__')
        ordering = ['-publish_time']