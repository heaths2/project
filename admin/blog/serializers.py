from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'created_at', 'modified_at', 'url', 'author', 'title', 'content', 'image', 'files']


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'modified_at', 'url', 'post', 'content']