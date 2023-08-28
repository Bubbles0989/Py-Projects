from fizzbuzz import fizzbuzz

def test_fizzbuzz_2_returns_2():
    assert fizzbuzz(2) == 2

def test_fizzbuzz_21_returns_fizz():
    assert fizzbuzz(21) == 'fizz'

def test_fizzbuzz_35_returns_buzz():
    assert fizzbuzz(35) == 'buzz'

def test_fizzbuzz_30_returns_fizzbuzz():
    assert fizzbuzz(30) == 'fizzbuzz'

def test_fizzbuzz_negative_returns_informational_message():
    assert fizzbuzz(-10) == 'Numbers between 1 and 100 please.'

def test_fizzbuzz_over_100_returns_informational_message():
    assert fizzbuzz(101) == 'Numbers between 1 and 100 please.'