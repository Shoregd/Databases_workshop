As a coach
So I can get to know all students
I want to keep a list of students' names.

As a coach
So I can get to know all students
I want to assign tags to students (for example, "happy", "excited", etc).

As a coach
So I can get to know all students
I want to be able to assign the same tag to many different students.

As a coach
So I can get to know all students
I want to be able to assign many different tags to a student.

--- NOUNS ---

students,name,tags

--- TABLE LAYOUT ---

RECORD | PROPERTIES

students | name

tags    | name

--- DATA TYPES ---

students:
    * id: SERIAL
    * name: text

tags:
    * id: SERIAL
    * name:text

--- RELATIONSHIPS ---

A student can have MANY tags. A tag can have MANY students

--- JOIN TABLE ---

join table for tables: students and tags
join table name: students_tags
Columns: student_id, tag_id