from rest_framework import serializers

from .models import Forum, Post, User


# add stuff here so that the data can be accesses viewed in API
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username')


class ForumSerializer(serializers.ModelSerializer):
    # user = UserSerializer()  # now username will be displayed instead of the num
    # user = serializers.CharField(source='user.username', read_only=True)  # FINALLY WORKS

    class Meta:
        model = Forum
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # username = serializers.CharField(source='user.username', read_only=True)  # FINALLY WORKS

    class Meta:
        model = Post
        fields = '__all__'
        # depth = 1
