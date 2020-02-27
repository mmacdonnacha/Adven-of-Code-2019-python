# Opcode 1 adds
# Opcode 2 multiplies
# Opcode 99 finish / exit program

# [a, b, c, d]
# a is opcode
# b is a number
# c is a number
# d is location index of result to be stored


def part1(intcode):
    intcode = [int(i) for i in intcode]
    
    for index in range(0, len(intcode), 4):
        opcode = intcode[index]
        if opcode == 1:
            a = intcode[index+1]
            b = intcode[index+2]
            c = intcode[index+3]
            intcode[c] = intcode[a] + intcode[b]
        elif opcode == 2:
            a = intcode[index+1] 
            b = intcode[index+2]
            c = intcode[index+3] 
            intcode[c] = intcode[a] * intcode[b]
        elif opcode == 99:
            break
    
    return intcode

def part2(intcode):
    for noun in range(0, 100):
        for verb in range(0, 100):
            intcode[1] = noun
            intcode[2] = verb

            if(part1(intcode)[0] == 19690720):
                return noun, verb


def solve():
    part1_answer = 0

    with open('input') as f: 
        for line in f: 
            intcode = line.strip('\n').split(',')
            
        part1_list = list.copy(intcode)
        part1_list[1] = 12
        part1_list[2] = 2
        part1_answer = part1(part1_list)

        part2_list = list.copy(intcode)
        part2_answer = part2(part2_list)

    print(f'Part 1: {part1_answer[0]}')
    print(f'Part 1: {100 * part2_answer[0] + part2_answer[1]}')



if __name__ in '__main__':
    solve()
