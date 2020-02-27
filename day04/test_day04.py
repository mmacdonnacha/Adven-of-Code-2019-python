import day04

def test_only_increasing():
   number  = 1
   assert day04.only_increasing(number) == True

def test_only_increasing_a():
   number  = 11
   assert day04.only_increasing(number) == True

def test_only_increasing_b():
   number  = 10
   assert day04.only_increasing(number) == False

def test_only_increasing_c():
   number  = 123
   assert day04.only_increasing(number) == True

def test_only_increasing_c():
   number  = 132
   assert day04.only_increasing(number) == False

def test_only_increasing_c():
   number  = 321
   assert day04.only_increasing(number) == False

def test_contains_doubles():
    number = 1
    assert day04.contains_doubles(number) == False

def test_contains_doubles_a():
    number = 10
    assert day04.contains_doubles(number) == False

def test_contains_doubles_b():
    number = 11
    assert day04.contains_doubles(number) == True

def test_ending_with_a_double():
    number = 122
    assert day04.ending_with_a_double(number) == True
