
DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;
DROP TABLE IF EXISTS cohorts;
DROP SEQUENCE IF EXISTS cohorts_id_seq;

CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  starting_date date
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id) references cohorts(id) on delete cascade
);



INSERT INTO cohorts (name,starting_date) VALUES('October2023RA','2023-10-30');
INSERT INTO cohorts (name,starting_date) VALUES('October2023R1','2023-10-30');

INSERT INTO students (name,cohort_id) VALUES('Greg Smith',1);
INSERT INTO students (name,cohort_id) VALUES('Terry Bloggs',1);
INSERT INTO students (name,cohort_id) VALUES('John Doe',1);
INSERT INTO students (name,cohort_id) VALUES('Greg Doe',2);
INSERT INTO students (name,cohort_id) VALUES('Terry Smith',2);
INSERT INTO students (name,cohort_id) VALUES('John Bloggs',2);