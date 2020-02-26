import day01

def test_part1_mass_of_12():
   mass = 12
   assert day01.part1(mass) == 2


def test_part1_mass_of_14():
   mass = 14
   assert day01.part1(mass) == 2


def test_part1_mass_of_1969():
   mass = 1969
   assert day01.part1(mass) == 654


def test_part1_mass_of_100756():
   mass = 100756
   assert day01.part1(mass) == 33583


def test_part2_mass_of_14():
    mass = 14
    assert day01.part2(mass) == 2

def test_part2_mass_of_1969():
    mass = 1969
    assert day01.part2(mass) == 966

def test_part2_mass_of_100756():
    mass = 100756
    assert day01.part2(mass) == 50346
