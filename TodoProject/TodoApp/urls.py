from django.urls import path, include
from rest_framework import routers
from .views import TodoViewset

router = routers.DefaultRouter()
router.register("todo", TodoViewset)

urlpatterns = [
    path('', include(router.urls)),
]