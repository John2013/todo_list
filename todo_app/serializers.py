from django.contrib.auth.models import User, Group
from rest_framework import serializers

from todo_app import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "description",
        )
        model = models.Todo
