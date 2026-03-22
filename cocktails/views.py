from rest_framework import viewsets, permissions
from .models import Ingredient, Cocktail
from .serializers import IngredientSerializer, CocktailSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    """Pozwala na edycję/usunięcie tylko autorowi lub adminowi."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]

    filterset_fields = ['category', 'author']
    search_fields = ['name', 'instructions']
    ordering_fields = ['name', 'id']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)