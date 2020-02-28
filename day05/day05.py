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
        if opcode in [1,2,3,4,5,6,7,8,99]:
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
                user_input = int(input('Enter input> '))
                # user_input = 1
                # print(f'User input> {user_input}')
                a = intcode[index+1]
                intcode[a] = user_input
                index += 2
            elif opcode == 4: # print to screen
                a = intcode[index+1]
                index += 2
                print(intcode[a])
            elif opcode == 99: # exit
                break

        else:
            temp = '0' + str(opcode)
            op_list = [int(d) for d in temp]
            del op_list[-2]

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
            elif opcode == 99: # exit
                break
            
    
    return intcode 

def part2(intcode):
    intcode = [int(i) for i in intcode]
    index = 0
    while index < len(intcode):
        opcode = intcode[index]
        if opcode in [1,2,3,4,5,6,7,8,99]:
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
                user_input = int(input('Enter input> '))
                # user_input = 1
                # print(f'User input> {user_input}')
                a = intcode[index+1]
                intcode[a] = user_input
                index += 2
            elif opcode == 4: # print to screen
                a = intcode[index+1]
                index += 2
                print(intcode[a])
            elif opcode == 5: # jump-if-true
                a = intcode[index+1]
                b = intcode[index+2]
                if intcode[a] == 0:
                    index += 3
                else:
                    index = intcode[b]
            elif opcode == 6: # jump-if-false
                a = intcode[index+1]
                b = intcode[index+2]
                if intcode[a] != 0:
                    index += 3
                else:
                    index = intcode[b]
            elif opcode == 7: # less than
                a = intcode[index+1]
                b = intcode[index+2]
                c = intcode[index+3]

                if intcode[a] < intcode[b]:
                    intcode[c] = 1
                else:
                    intcode[c] = 0
                index += 4
            elif opcode == 8: # equals
                a = intcode[index+1]
                b = intcode[index+2]
                c = intcode[index+3]
                if  intcode[a] == intcode[b]:
                    intcode[c] = 1
                else:
                    intcode[c] = 0
                index += 4
            elif opcode == 99: # exit
                break

        else:
            temp = '0' + str(opcode)
            op_list = [int(d) for d in temp]
            del op_list[-2]

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
                # print(intcode[a])
            elif opcode == 5: # jump-if-true
                a = intcode[index+1]
                b = intcode[index+2]
                c = intcode[index+3]

                if op_list[-2] == 0:
                    a = intcode[a]
                    
                if op_list[-3] == 0:
                    b = intcode[b]

                if a != 0:
                    index = b
                else:
                    index += 3
            elif opcode == 6: # jump-if-false
                a = intcode[index+1]
                b = intcode[index+2]
                c = intcode[index+3]

                if op_list[-2] == 0:
                    a = intcode[a]
                    
                if op_list[-3] == 0:
                    b = intcode[b]
                
                if a == 0:
                    index = b
                else:
                    index += 3
            elif opcode == 7: # less than
                a = intcode[index+1]
                b = intcode[index+2]
                c = intcode[index+3]

                if op_list[-2] == 0:
                    a = intcode[a]
                    
                if op_list[-3] == 0:
                    b = intcode[b]

                if  a < b:
                    intcode[c] = 1
                else:
                    intcode[c] = 0
                index += 4
            elif opcode == 8: # equals
                a = intcode[index+1]
                b = intcode[index+2]
                c = intcode[index+3]

                if op_list[-2] == 0:
                    a = intcode[a]
                    
                if op_list[-3] == 0:
                    b = intcode[b]

                if  a == b:
                    intcode[c] = 1
                else:
                    intcode[c] = 0
                index += 4
            elif opcode == 99: # exit
                break
            
    return intcode 


def solve():
    part1_answer = 0

    with open('input') as f: 
        for line in f: 
            intcode = line.strip('\n').split(',')
            
        # part1_list = list.copy(intcode)
        # part1_answer = part1(part1_list)

        part2_list = list.copy(intcode)
        part2_answer = part2(part2_list)

    # print(f'Part 1: {part1_answer[0]}')
    # print(f'Part 2: {100 * part2_answer[0] + part2_answer[1]}')



if __name__ in '__main__':
    solve()
    # print(part1([3,0,4,0,99]))
    # print(part1([1002,4,3,4,33]))
    # print(part1([1101,100,-1,4,0]))
    # print(part1([3,9,8,9,10,9,4,9,99,-1,8]))
    # print(part1([3,9,7,9,10,9,4,9,99,-1,8]))
    # print(part1([3,3,1108,-1,8,3,4,3,99]))
    # print(part1([3,3,1107,-1,8,3,4,3,99]))
    print('###########################')
    # print(part1([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]))
    # print(part1([3,3,1105,-1,9,1101,0,0,12,4,12,99,1]))
    # print(part1([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]))
