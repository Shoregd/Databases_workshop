from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self,connection):
        self._connection = connection
    def all(self):
        rows = self._connection.execute(
            'SELECT * from recipes'
        )
        recipes = []
        for row in rows:
            data = Recipe(row['id'],row['recipe_name'],row['cooking_time'],row['rating'])
            recipes.append(data)

        return recipes
    def find(self,recipe_id):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s',[recipe_id]
        )
        row = rows[0]
        return Recipe(row['id'],row['recipe_name'],row['cooking_time'],row['rating'])
