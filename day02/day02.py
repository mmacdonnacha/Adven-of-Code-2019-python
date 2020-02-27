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


def solve():
    part1_answer = 0

    with open('input') as f: 
        for line in f: 
            intcode = line.strip('\n').split(',')
            
        part1_list = list.copy(intcode)
        part1_list[1] = 12
        part1_list[2] = 2
        part1_answer = part1(part1_list)

    print(f'Part 1: {part1_answer[0]}')



if __name__ in '__main__':
    solve()


