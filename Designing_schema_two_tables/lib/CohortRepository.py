from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    def __init__(self,connection):
        self._connection = connection

    def get_cohort(self,cohort_id):
        rows = self._connection.execute(
            'SELECT * FROM cohorts WHERE id = %s',[cohort_id]
            )
        row = rows[0]
        return Cohort(row['id'],row['name'],str(row['starting_date']))
    def find_with_students(self,cohort_number):
        return_data =[]
        student_list = []
        rows = self._connection.execute(
            '''
            SELECT
                    cohorts.id as cohorts_id,
                    cohorts.name as cohort_name,
                    cohorts.starting_date,
                    students.id as student_id,
                    students.name as student_name,
                    students.cohort_id
            FROM cohorts
            JOIN students
            ON cohorts.id = students.cohort_id
            WHERE cohorts.id = %s
            ''', [cohort_number]
        )
        data = Cohort(rows[0]['cohorts_id'],rows[0]['cohort_name'],str(rows[0]['starting_date']))
        return_data.append(data)
        for row in rows:
            data = Student(row['student_id'],row['student_name'],row['cohort_id'])
            student_list.append(data)  
        return_data.append(student_list)
        
        return return_data