from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/comments/', include('daomi.comments.api.urls', namespace='api-comments')),
    # path(f'{BASE_URL}/', include(router.urls)),
]
