from django.db import models
from django.contrib.auth.models import User

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    is_alcoholic = models.BooleanField(default=False)
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name

class Cocktail(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='cocktails')
    ingredients = models.ManyToManyField(Ingredient, through='CocktailIngredient', related_name='cocktails')

    def __str__(self):
        return self.name

class CocktailIngredient(models.Model):
    """
    Tabela pośrednia. Łączy konkretny koktajl z konkretnym składnikiem
    i przechowuje informację o dokładnych ilościach/proporcjach (wymóg z zadania).
    """
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)

    class Meta:
        unique_together = ('cocktail', 'ingredient')

    def __str__(self):
        return f"{self.amount} of {self.ingredient.name} in {self.cocktail.name}"