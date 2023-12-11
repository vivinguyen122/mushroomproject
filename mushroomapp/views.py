from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import status

# def index(request):
#     forums = Forum.objects.all()
#     return render(request, 'index.html', {'forums': forums})


class SearchView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', '')

        # Search for posts with titles containing the query
        posts = Post.objects.filter(title__icontains=query)
        post_serializer = PostSerializer(posts, many=True)

        # Search for forums with titles containing the query
        forums = Forum.objects.filter(title__icontains=query)
        forum_serializer = ForumSerializer(forums, many=True)

        result_data = {
            'posts': post_serializer.data,
            'forums': forum_serializer.data,
        }

        return Response(result_data, status=status.HTTP_200_OK)

class ForumApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # get all forum posts data
    def get(self, request, *args, **kwargs):  # get list of posts WORKS ----------
        posts = Forum.objects
        serializer = ForumSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):  # add new post WORKS
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'username': request.data.get('username')

            # 'user': request.user.id,
        }

        serializer = ForumSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ForumDetailView(APIView):  # get specific forum
    def get_obj(self, forum_id):
        try:
            return Forum.objects.get(id=forum_id)
        except Forum.DoesNotExist:
            return None

    def get(self, request, forum_id, *args, **kwargs):  # based on id, grab the info. needs get_obj() from above WORKS --
        forum_instance = self.get_obj(forum_id)
        if not forum_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = ForumSerializer(forum_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, forum_id, *args, **kwargs):  # update by the id WORKS -------
        forum_instance = self.get_obj(forum_id)
        if not forum_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = {
            'title': request.data.get('title', forum_instance.title),  # optional for user to edit fields
            'description': request.data.get('description', forum_instance.description),
            'favourite': request.data.get('favourite', forum_instance.favourite)
        }

        serializer = ForumSerializer(instance=forum_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, forum_id, *args, **kwargs):  # deletes the WORKS ----------
        forum_instance = self.get_obj(forum_id)
        if not forum_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        forum_instance.delete()

        return Response(status=status.HTTP_200_OK)



# from my po2

class PostApiView(APIView):
    def get(request, *args, **kwargs):  # get list of posts WORKS ----------
        posts = Post.objects
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):  # add new post WORKS
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'username': request.data.get('username')
            # 'img': request.data.get('img'),
            # 'user': request.user.id,  # user who's logged in is the one whose id is automatically placed
            # 'user': request.data.get('user')
        }

        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):  # get specific post. add request.user.id if want to make it view by same account only
    def get_obj(self, post_id):
        try:
            return Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return None

    def get(self, request, post_id, *args, **kwargs):  # based on id, grab the info. needs get_obj() from above WORKS --
        post_instance = self.get_obj(post_id)
        if not post_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = PostSerializer(post_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, post_id, *args, **kwargs):  # update post by the id WORKS -------
        post_instance = self.get_obj(post_id)
        if not post_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = {
            'title': request.data.get('title', post_instance.title),  # optional for user to edit fields
            'description': request.data.get('description', post_instance.description),
            'img': request.data.get('img', post_instance.img),
            'favourite': request.data.get('favourite', post_instance.favourite)
        }

        if 'img' not in request.data:  # lets me update and not get error because didn't put an img
            del data['img']

        serializer = PostSerializer(instance=post_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id, *args, **kwargs):  # deletes the post WORKS ----------
        post_instance = self.get_obj(post_id)
        if not post_instance:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        post_instance.delete()

        return Response(status=status.HTTP_200_OK)

