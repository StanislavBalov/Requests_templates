from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipe_view(request, recipe_name):
    if recipe_name not in DATA:
        raise Http404("Recipe not found")
    
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        raise Http404("Invalid servings value")
    
    recipe = {ingredient: amount * servings for ingredient, amount in DATA[recipe_name].items()}
    context = {'recipe': recipe}

    return render(request, 'recipe.html', context)
