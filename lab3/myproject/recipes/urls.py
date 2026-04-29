from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/favorites/', views.profile_favorites, name='profile-favorites'),
    path('recipes/', views.recipe_list, name='recipe-list'),
    path('recipes/<int:recipe_id>/', views.recipe_detail, name='recipe-detail'),
    path('categories/<int:category_id>/', views.category_recipes, name='category-recipes'),
    path('favorites/add/', views.add_to_favorites, name='add-favorite'),
    path('favorites/remove/', views.remove_from_favorites, name='remove-favorite'),
]
