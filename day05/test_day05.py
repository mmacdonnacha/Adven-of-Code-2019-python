import day05

def test_part1_a():
   opcode = [1,9,10,3,2,3,11,0,99,30,40,50]
   answer = [3500,9,10,70,2,3,11,0,99,30,40,50]
   assert day05.part1(opcode) == answer


def test_part1_b():
   opcode = [1,0,0,0,99]
   answer = [2,0,0,0,99]
   assert day05.part1(opcode) == answer

def test_part1_c():
   opcode = [2,3,0,3,99]
   answer = [2,3,0,6,99]
   assert day05.part1(opcode) == answer

def test_part1_d():
   opcode = [2,4,4,5,99,   0] 
   answer = [2,4,4,5,99,9801]
   assert day05.part1(opcode) == answer

def test_part1_e():
   opcode = [ 1,1,1,4,99,5,6,0,99]
   answer = [30,1,1,4, 2,5,6,0,99]
   assert day05.part1(opcode) == answer

def test_part1_day05_a():
   opcode = [1002,4,3,4,33]
   answer = [1002,4,3,4,99]
   assert day05.part1(opcode) == answer

def test_part1_day05_b():
   opcode = [1101,100,-1,4, 0]
   answer = [1101,100,-1,4,99]
   assert day05.part1(opcode) == answer
 