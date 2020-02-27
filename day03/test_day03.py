import day03

def test_part1_a():
   first_path  = ['R8', 'U5', 'L5', 'D3']
   second_path = ['U7', 'R6', 'D4', 'L4']
   answer = 6
   assert day03.part1(first_path, second_path) == answer

def test_part1_b():
   first_path  = ['R75','D30','R83','U83','L12','D49','R71', 'U7','L72']
   second_path = ['U62','R66','U55','R34','D71','R55','D58','R83']
   answer = 159
   assert day03.part1(first_path, second_path) == answer

def test_part1_c():
   first_path  = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
   second_path = ['U98','R91','D20','R16','D67','R40', 'U7','R15', 'U6', 'R7']
   answer = 135
   assert day03.part1(first_path, second_path) == answer

def test_part2_a():
   first_path  = ['R8', 'U5', 'L5', 'D3']
   second_path = ['U7', 'R6', 'D4', 'L4']
   answer = 30
   assert day03.part2(first_path, second_path) == answer

def test_part2_b():
   first_path  = ['R75','D30','R83','U83','L12','D49','R71', 'U7','L72']
   second_path = ['U62','R66','U55','R34','D71','R55','D58','R83']
   answer = 610
   assert day03.part2(first_path, second_path) == answer

def test_part2_c():
   first_path  = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
   second_path = ['U98','R91','D20','R16','D67','R40', 'U7','R15', 'U6', 'R7']
   answer = 410
   assert day03.part2(first_path, second_path) == answer
