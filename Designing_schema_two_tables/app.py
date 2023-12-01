from lib.database_connection import DatabaseConnection
from lib.CohortRepository import CohortRepository
from lib.PostRepository import PostRepository



# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog_setup.sql")

#repository = CohortRepository(connection)
#print('Return value for calling get_cohort(1):\n')
#print(' ',repository.get_cohort(1),'\n')

#print('Return value for find_with_students(1): (Cleaned up)\n')
#result = repository.find_with_students(1)

#for item in result:
#    if type(item) != list:
#        print(' ',f'{item}:')
#    else:
#        for data in item:
#            print('     ',data)

repository = PostRepository(connection)

print('Return value for post_with_comments(1):\n')
print(' ',repository.post_with_comments(1),'\n')
print('Return value for post_with_comments(1): (Cleaned up)\n')
result = repository.post_with_comments(1)
for item in result:
    if type(item) != list:
        print(' ',f'{item}:')
    else:
        for data in item:
            print('     ',data)