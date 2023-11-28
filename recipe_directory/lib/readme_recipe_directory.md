As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).

--- NOUNS ---
 * Recipes
 * recipe_name
 * cooking_time
 * rating


--- TABLE LAYOUT ---

RECORD | PROPERTIES

Recipe | id, recipe_name, cooking_time, rating

--- DATA TYPES ---

 * id: Serial
 * recipe_name: text
 * cooking_time: int
 * rating: int

sql file = recipe_directory.sql


--- CLASSES ---

 * RecipeRepository - Repository class
    * contains a list of Recipe classes. 
    * all(): returns a list of all stored recipes
 * Recipe - Model class
    * Single instance of a recipe
    * Init:
        * id: Serial
        * recipe_name: string
        * cooking_time: int
        * rating: int
    * __repr__:
        * returns Recipe(id,recipe_name,cooking_time,rating)

    * __eq__:
        * takes self and other
        * returns if this __dict__ == other __dict__