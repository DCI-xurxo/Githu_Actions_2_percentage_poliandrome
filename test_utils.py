from utils import percentage_calculator, is_palindrome

def test_percentage_calculator():
    assert test_percentage_calculator(20,10) == 2
    assert test_percentage_calculator(0,100) == 0
    assert test_percentage_calculator(5,0) == 0

    def test_is_paliandrome():
        assert is_palindrome("madam")
        assert is_palindrome("rececar")
        assert is_palindrome("Good Morning")