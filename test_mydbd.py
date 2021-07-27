import mydbd


def test_calc_total():
    total = mydbd.calc_total(4, 5)
    assert total == 9


