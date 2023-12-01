from lib.student import Student

def test_init_holds_correct_info():
    test_student = Student(1,'Greg Smith',1)
    assert test_student.id == 1
    assert test_student.name == 'Greg Smith'
    assert test_student.cohort_id == 1

def test_class_repr_format():
    test_student = Student(1,'Greg Smith',1)
    assert str(test_student) == 'Student(1, Greg Smith, 1)'

def test_eq_allows_testing():
    test_student = Student(1,'Greg Smith',1)
    assert test_student == Student(1,'Greg Smith',1)

    