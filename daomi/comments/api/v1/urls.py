from rest_framework.routers import DefaultRouter

from daomi.comments.api.v1.views import CommentsViewSet

app_name = 'v1'

router = DefaultRouter()
router.register('comment', CommentsViewSet, basename='comments')

urlpatterns = router.urls