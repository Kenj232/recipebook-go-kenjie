from django.contrib import admin
from.models import Recipe, RecipeIngredient,Ingredient

class RecipeIngredientInline(admin.TabularInline):
    model =  RecipeIngredient
class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]

# Register your models here.
admin.site.register(Recipe, RecipeAdmin)