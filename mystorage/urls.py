from rest_framework.routers import DefaultRouter
from django.urls import path,include
from mystorage import views
from rest_framework import urls
router=DefaultRouter()
router.register('essay',views.PostViewSet)
router.register('album',views.ImageViewSet)
router.register('files',views.FileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
