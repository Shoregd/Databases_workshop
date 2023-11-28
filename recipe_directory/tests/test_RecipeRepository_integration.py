from lib.recipe import Recipe
from lib.RecipeRepository import RecipeRepository

def test_recipe_repo_returns_all_records(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
        Recipe(1, 'Lasagna', 45,4),
        Recipe(2, 'Tacos', 25,5),
        Recipe(3, 'Kimchi', 90,3),
        Recipe(4, 'Tiramasu', 35,4),
        Recipe(5, 'Spaghetti Meatballs', 40,5)
    ]

def test_find_single_recipe_by_id(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)

    assert repository.find(3) == Recipe(3, 'Kimchi', 90,3)