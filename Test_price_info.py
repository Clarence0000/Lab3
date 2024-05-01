import price_info

def test_total_cost_shopping():
    test_value = 46.75

    result = price_info.total_cost_shopping()

    assert (test_value == result)

def test_cost_of_fruit():
    
    test_value = 69.3

    result = price_info.cost_of_fruits('pomegranate' , 14)

    assert (result == test_value)