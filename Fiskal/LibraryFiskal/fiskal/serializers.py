from rest_framework import serializers
from core.models import Book, AudioBook, Article, Work, Event, Tag
from comments.models import Comment
from rate.models import Rate


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class AudioBookSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = AudioBook
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    tag = TagSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)

    class Meta:
        model = Work
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from rate.models import Rate

from rest_framework import serializers
from rate.models import Rate

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'
