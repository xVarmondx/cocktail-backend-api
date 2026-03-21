from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, CocktailViewSet

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'cocktails', CocktailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]