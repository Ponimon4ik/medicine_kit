from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DrugViewSet

router_v1 = DefaultRouter()
router_v1.register('drugs', DrugViewSet, basename='drug')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('users.urls'))
]
