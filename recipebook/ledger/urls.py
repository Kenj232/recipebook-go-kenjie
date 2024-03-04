from django.urls import path
from .views import recipe, recipe_detail


urlpatterns = [
    path('recipes/list',recipe, name="recipes"),
    path('recipe/<int:id>/detail',recipe_detail, name='recipe_detail'),

]

app_name = "ledger"