import day06

def test_part1():
   solar_system = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
   answer = 42
   assert day06.part1(solar_system) == answer

def test_part1_alternate_ordering():
   solar_system = ['K)L','J)K','E)J','D)I','G)H','B)G','E)F','D)E','C)D','B)C','COM)B']
   answer = 42
   assert day06.part1(solar_system) == answer

def test_part2():
    solar_system = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']
    answer = 4
    assert day06.part2(solar_system) == answer