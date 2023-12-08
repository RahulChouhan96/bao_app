# myapp/urls.py
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, get_all_films
from django.urls import path


router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
# urlpatterns = router.urls


urlpatterns = [
    # ... your other URLs
    path('get_all_films/', get_all_films, name='get_all_films'),
]
