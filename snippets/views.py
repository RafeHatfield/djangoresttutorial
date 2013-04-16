from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

class SnippetList(permissions.IsAuthenticatedOrReadOnly, generics.ListCreateAPIView):
    model = Snippet
    serializer_class = SnippetSerializer

    def pre_save(self, obj):
        obj.owner = self.request.user

class SnippetDetail(permissions.IsAuthenticatedOrReadOnly, generics.RetrieveUpdateDestroyAPIView):
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer