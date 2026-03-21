from django.contrib import admin
from .models import Ingredient, Cocktail, CocktailIngredient

class CocktailIngredientInline(admin.TabularInline):
    model = CocktailIngredient
    extra = 1

class CocktailAdmin(admin.ModelAdmin):
    inlines = [CocktailIngredientInline]

admin.site.register(Ingredient)
admin.site.register(Cocktail, CocktailAdmin)