import Lab2.bmi as bmi

def test_bmi_normal_weight():
    assert (bmi.calculate_bmi(1.73,57) == 0)
def test_bmi_over_weight():
    assert (bmi.calculate_bmi(1.73,100.0) == 1)
def test_bmi_under_weight():
    assert (bmi.calculate_bmi(1.73,20.0) == -1)