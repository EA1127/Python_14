from rest_framework import rendererc, viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serialzers import SnippetSerializer, UserSerializer

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(deatil=True, renderer_classes = [renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self/get_object(
        return Response(snippet.highlighted)
    

    def perform_create(self_serializer):
        serializer.save(owner=self/request/user)


class UserViewSet(viewsets.ReadOnlyModelSet):
    queryset = User.objects.all
    serializer_class = UserSerializer

