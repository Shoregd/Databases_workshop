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
