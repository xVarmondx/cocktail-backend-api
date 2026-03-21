from rest_framework import viewsets, permissions
from .models import Ingredient, Cocktail
from .serializers import IngredientSerializer, CocktailSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filterset_fields = ['is_alcoholic']
    search_fields = ['name', 'description']
    ordering_fields = ['name']


class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filterset_fields = ['category', 'author']
    search_fields = ['name', 'instructions']
    ordering_fields = ['name', 'id']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)