from lib.cohort import Cohort

def test_init_correct():
    test_cohort = Cohort(1,'October2023RA','2023-10-30')
    assert test_cohort.id == 1
    assert test_cohort.name == 'October2023RA'
    assert test_cohort.starting_date == '2023-10-30'

def test_repr_format():
    test_cohort = Cohort(1,'October2023RA','2023-10-30')
    assert str(test_cohort) == 'Cohort(1, October2023RA, 2023-10-30)'

def test_eq_for_tests():
    test_cohort = Cohort(1,'October2023RA','2023-10-30')
    assert test_cohort == Cohort(1,'October2023RA','2023-10-30')