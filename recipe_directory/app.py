from lib.database_connection import DatabaseConnection
from lib.RecipeRepository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipe_directory.sql")

repository = RecipeRepository(connection)

result = repository.all()

for item in result:
    print(item)

result = repository.find(3)

print(result)