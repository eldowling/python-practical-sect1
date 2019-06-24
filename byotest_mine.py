def is_even(number):
    cnt = 0
    if number % 2 == 0:
        cnt += 1
        
    return cnt

def number_of_evens(numbers):
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)


def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_is_not_in(collection, item):
    assert item not in collection, "{0} contains {1}".format(collection, item)
    
def test_is_between(item, a, b)
    assert item in range(a, b), "{0} is not between {1} and {2}".format(item, a, b)
    


#test_are_equal(number_of_evens([1,2,3,4,5]), 2)
test_is_between(5, 2, 7)