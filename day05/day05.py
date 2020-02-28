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
    index = 0
    while index < len(intcode):
        opcode = intcode[index]
        if opcode == 1: # addition
            a = intcode[index+1]
            b = intcode[index+2]
            c = intcode[index+3]
            intcode[c] = intcode[a] + intcode[b]
            index += 4
        elif opcode == 2: # mulitplication
            a = intcode[index+1] 
            b = intcode[index+2]
            c = intcode[index+3] 
            intcode[c] = intcode[a] * intcode[b]
            index += 4
        elif opcode == 3: # prompt for input
            # user_input = int(input('Enter input> '))
            user_input = 1
            print(f'User input> {user_input}')
            a = intcode[index+1]
            intcode[a] = user_input
            index += 2
        elif opcode == 4: # print to screen
            a = intcode[index+1]
            index += 2
            print(intcode[a])
        elif opcode == 99: # exit
            break

        elif opcode > 99:
            temp = '0' + str(opcode)
            op_list = [int(d) for d in temp]
            # for x in range(len(str(opcode))-1, 0, -1):
            #     op_list.append(int(str(op_list[x])))
            # op_list.remove(1)
            del op_list[-2]
            # print(f'{op_list} +++ {opcode}')

            
            opcode = op_list[-1]
            if opcode == 1: # addition
                if op_list[-2] == 1:
                    a = intcode[index+1]
                else:
                    a = intcode[index+1] # a = index of value
                    a = intcode[a]
                    
                if op_list[-3] == 1:
                    b = intcode[index+2]
                else:
                    b = intcode[index+2]
                    b = intcode[b]

                c = intcode[index+3]
                intcode[c] = a + b
                index += 4
            elif opcode == 2: # mulitplication
                if op_list[-2] == 1:
                    a = intcode[index+1]
                else:
                    a = intcode[index+1] # a = index of value
                    a = intcode[a]
                    
                if op_list[-3] == 1:
                    b = intcode[index+2]
                else:
                    b = intcode[index+2]
                    b = intcode[b]

                c = intcode[index+3] 
                intcode[c] = a * b
                index += 4
            elif opcode == 3: # prompt for input
                # user_input = int(input('Enter input> '))
                user_input = 1
                print(f'User input> {user_input}')
                a = intcode[index+1]
                intcode[a] = user_input
                index += 2
            elif opcode == 4: # print to screen
                if op_list[-2] == 1:
                    a = intcode[index+1]
                else:
                    a = intcode[index+1] # a = index of value
                    a = intcode[a]
                print(a)
                index += 2
                print(intcode[a])
            elif opcode == 99: # exit
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
        part1_answer = part1(part1_list)

        # part2_list = list.copy(intcode)
        # part2_answer = part2(part2_list)

    # print(f'Part 1: {part1_answer[0]}')
    # print(f'Part 2: {100 * part2_answer[0] + part2_answer[1]}')



if __name__ in '__main__':
    solve()
    # print(part1([3,0,4,0,99]))
    # print(part1([1002,4,3,4,33]))
    # print(part1([1101,100,-1,4,0]))
