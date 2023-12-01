from lib.CohortRepository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student


def test_system_can_return_cohort(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    result = repository.get_cohort(1)
    assert result == Cohort(1,'October2023RA','2023-10-30')


def test_system_can_return_students_for_given_cohort(db_connection):
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    result = repository.find_with_students(1)

    assert result == [
        Cohort(1,'October2023RA','2023-10-30'),
        [
            Student(1, 'Greg Smith',1),
            Student(2, 'Terry Bloggs',1),
            Student(3, 'John Doe',1)
        ]
        
        ]