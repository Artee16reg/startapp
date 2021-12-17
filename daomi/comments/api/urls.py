from django.urls import path, include

from daomi.comments.apps import CommentConfig

app_name = CommentConfig.name

urlpatterns = [
    path('v1/', include('daomi.comments.api.v1.urls', namespace='v1'))
]