from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from daomi.comments.api.v1.serializers import CommentsSerializer
from daomi.comments.models import Comment


class CommentsViewSet(viewsets.ModelViewSet):
    """CommentViewset."""

    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
