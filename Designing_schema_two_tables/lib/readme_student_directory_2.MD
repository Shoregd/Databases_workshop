As a coach
So I can get to know all students
I want to see a list of students' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' names.

As a coach
So I can get to know all students
I want to see a list of cohorts' starting dates.

As a coach
So I can get to know all students
I want to see a list of students' cohorts.

--- NOUNS ---

 * Students
 * Cohorts
 * name
 * starting_date


--- TABLE LAYOUT ---

students:

RECORD | PROPERTIES

student | name

cohorts:

RECORD | PROPERTIES

cohort | name, starting_date

--- DATA TYPES ---

students:
 * name: text

cohorts:
 * name: text
 * starting_date: int

--- RELATIONSHIPS ---

Cohort can have many students. Student belongs to cohort. Student has the foreign key.

SQL already exists in file student_directory_2.sql

--- CLASS SETUP ---

 * Student: Model Class
    * __init__: name, cohort_id, cohort default to []
    * __repr__: Student(name, cohort_id)
    * __eq__: Allow for testing

 * Cohort: Model Class
    * __init__: name, starting_date
    * __repr__: Cohort(name, starting_date)
    * __eq__: Allow for testing

 * CohortRepository: Repository Class
    * __init__: Database connection
    * _get_cohort_data: will take the cohort id and return the corresponding cohort class 'SELECT * FROM cohorts WHERE id = %s',[cohort_id] 

    I.e get_cohort(1) returns Cohort(1,'October2023RA','2023-10-30')
    * find_with_students: take the cohort id and return the cohort name, starting_date followed by the list of students. 
    
    I.e find_with_students(1) would return [Cohort(1,'October2023RA','2023-10-30'),[Student(1,'Greg Smith',1),Student(2,'Terry Bloggs',1),Student(3,'John Doe',1)]] executing 
    'SELECT 
            cohorts.id as cohorts_id,
            cohorts.name as cohort_name,
            cohorts.starting_date,
            students.id as student_id,
            students.name as student_name,
            students.cohort_id as cohort_id
    FROM COHORTS
    JOIN STUDENTS
    ON cohorts_id = cohort_id
    WHERE cohorts_id =%s', [cohort_number]
