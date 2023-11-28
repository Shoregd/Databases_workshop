from lib.recipe import Recipe

def test_init_correct():
    test_recipe = Recipe(1,'Test Recipe',25,1)
    assert test_recipe.id == 1
    assert test_recipe.recipe_name == 'Test Recipe'
    assert test_recipe.rating == 1
    assert test_recipe.cooking_time == 25

def test_recipe_format():
    test_recipe = Recipe(1,'Test Recipe',25,1)
    assert str(test_recipe) == 'Recipe(1, Test Recipe, 25, 1)'

def test_Recipes_equal_classes():
    test_recipe = Recipe(1,'Test Recipe',25,1)
    test_recipe2 = Recipe(1,'Test Recipe',25,1)
    assert test_recipe == test_recipe2