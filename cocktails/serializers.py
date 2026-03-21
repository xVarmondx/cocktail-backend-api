from rest_framework import serializers
from .models import Ingredient, Cocktail, CocktailIngredient
from django.core.validators import MinLengthValidator, RegexValidator


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class CocktailIngredientSerializer(serializers.ModelSerializer):
    ingredient_details = IngredientSerializer(source='ingredient', read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        queryset=Ingredient.objects.all(), source='ingredient', write_only=True
    )

    def validate_name(self, value):
        """Sprawdza, czy nazwa koktajlu ma co najmniej 3 znaki"""
        if len(value) < 3:
            raise serializers.ValidationError("Nazwa koktajlu jest za krótka. Musi mieć minimum 3 znaki.")
        return value

    def validate_category(self, value):
        """Sprawdza, czy kategoria nie zawiera cyfr"""
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Kategoria koktajlu nie może zawierać cyfr.")
        return value

    def create(self, validated_data):
        ingredients_data = validated_data.pop('cocktailingredient_set', [])
        cocktail = Cocktail.objects.create(**validated_data)

        for ingredient_data in ingredients_data:
            CocktailIngredient.objects.create(
                cocktail=cocktail,
                ingredient=ingredient_data['ingredient'],
                amount=ingredient_data['amount']
            )
        return cocktail

    class Meta:
        model = CocktailIngredient
        fields = ['ingredient_id', 'ingredient_details', 'amount']


class CocktailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[MinLengthValidator(3, message="Nazwa koktajlu musi mieć co najmniej 3 znaki.")]
    )
    category = serializers.CharField(
        validators=[RegexValidator(regex=r'^[a-zA-Z\s]*$', message="Kategoria może zawierać tylko litery i spacje.")]
    )

    ingredients = CocktailIngredientSerializer(source='cocktailingredient_set', many=True)
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'category', 'instructions', 'author', 'author_name', 'ingredients']
        read_only_fields = ['author']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('cocktailingredient_set', [])
        cocktail = Cocktail.objects.create(**validated_data)

        for ingredient_data in ingredients_data:
            CocktailIngredient.objects.create(
                cocktail=cocktail,
                ingredient=ingredient_data['ingredient'],
                amount=ingredient_data['amount']
            )
        return cocktail