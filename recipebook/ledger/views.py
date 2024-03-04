from django.shortcuts import render
from .models import Recipe, RecipeIngredient
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.http import HttpResponse

def recipe(request):
    recipe = Recipe.objects.all()
    ctx = {
    'recipes': recipe
    }
    return render(request, 'recipes_list.html', ctx)

def recipe_detail(request, id):
    ctx = { 
        'recipes': Recipe.objects.get(id=id),
        'ingredients': RecipeIngredient.objects.filter(recipe__id=id)
    }
    return render(request, 'recipe.html', ctx)


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes_list.html"

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe.html"
