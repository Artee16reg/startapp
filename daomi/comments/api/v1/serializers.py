from rest_framework import serializers

from daomi.comments.models import Comment


class CommentsSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField("%d-%m-%Y %T:%M%p")

    class Meta:
        model = Comment
        fields = '__all__'