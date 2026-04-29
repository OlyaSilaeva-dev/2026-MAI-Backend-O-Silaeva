from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def recipe_list(request):
    """Список всех рецептов"""
    recipes_data = [
        {"id": 1, "title": "Борщ", "category": "Суп", "author": "Михаил", "cooking_time": 90, "image": "http://example.com/borsch.jpg" },
        {"id": 2, "title": "Оливье", "category": "Салат", "author": "Анна", "cooking_time": 60, "image": ""},
    ]
    return JsonResponse(recipes_data, safe=False)

@require_http_methods(["GET"])
def recipe_detail(request, recipe_id):
    """Детальная страница рецептов"""
    recipe = {
        "id": recipe_id,
        "title": f"Рецепт {recipe_id}",
        "description": "Это описание рецепта-заглушки.",
        "ingredients": ["ингредиент 1", "ингредиент 2"],
        "steps": "Шаг 1... Шаг 2...",
        "category": "Десерт",
        "autor": "Пользователь",
        "cooking_time": 45
    }
    return JsonResponse(recipe, safe=False, json_dumps_params={'ensure_ascii': False})

@require_http_methods(["GET"])
def profile(request):
    """Профиль пользователя"""
    return JsonResponse({
        "id": 1,
        "username": "user",
        "email": "cook@example.com",
        "favorites_count": 5
    })
    
@require_http_methods(["GET"])
def profile_favorites(request):
    """Избранные рецепты пользователя"""
    favorites = [
        {"id": 1, "title": "Борщ", "added_at": "2025-01-01"},
        {"id": 3, "title": "Пирог", "added_at": "2025-01-02"}
    ]
    return JsonResponse(favorites, safe=False, json_dumps_params={'ensure_ascii': False})

@require_http_methods(["GET"])
def category_recipes(request, category_id):
    """Рецепты по категории"""
    categories = {
        1: {"id": 1, "name": "Супы", "recipes": [{"id": 1, "title": "Борщ"}]},
        2: {"id": 2, "name": "Салаты", "recipes": [{"id": 2, "title": "Оливье"}]},
    }
    if category_id in categories:
        return JsonResponse(categories[category_id], safe=False, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({"error": "Category not found"}, status=404)

@require_http_methods(["POST"])
def add_to_favorites(request, recipe_id):
    """Добавить рецепт в избранное"""
    return JsonResponse({"status": "added", "recipe_id": request.POST.get("recipe_id")})

@require_http_methods(["POST"])
def remove_from_favorites(request, recipe_id):
    """Удалить из избранного"""
    return JsonResponse({"status": "removed"})