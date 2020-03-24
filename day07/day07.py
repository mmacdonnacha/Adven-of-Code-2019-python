import itertools

# Opcode 1 adds
# Opcode 2 multiplies
# Opcode 99 finish / exit program

# [a, b, c, d]
# a is opcode
# b is a number
# c is a number
# d is location index of result to be stored

 

def part1(intcode, amp, value):
    intcode = [int(i) for i in intcode]
    index = 0
    first_run = True
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
                # user_input = int(input('Enter input> '))
                if first_run:
                    # print(f'Enter input> {amp}')
                    user_input = amp
                    first_run = False
                else:
                    # print(f'Enter input> {value}')
                    user_input = value
                # user_input = 1
                # print(f'User input> {user_input}')
                a = intcode[index+1]
                intcode[a] = user_input
                index += 2
            elif opcode == 4: # print to screen
                a = intcode[index+1]
                index += 2
                # print(intcode[a])
                value = intcode[a]
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
                # user_input = 1
                # print(f'User input> {user_input}')
                if first_run:
                    # print(f'Enter input> {amp}')
                    user_input = amp
                    first_run = False
                else:
                    # print(f'Enter input> {value}')
                    user_input = value

                a = intcode[index+1]
                intcode[a] = user_input
                index += 2
            elif opcode == 4: # print to screen
                if op_list[-2] == 1:
                    a = intcode[index+1]
                else:
                    a = intcode[index+1] # a = index of value
                    a = intcode[a]
                # print(a)
                value = a
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
            
    # return intcode
    return value 


def solve():
    part1_answer = 0

    with open('input') as f: 
        for line in f: 
            intcode = line.strip('\n').split(',')
        
    amplifier = list(itertools.permutations([0,1,2,3,4]))
    highest_thrust = 0
    highest_amp_settings = ()
    amp_list = []
    thrust_list = []

    for settings in amplifier:
        thrust = run(intcode, settings)
        amp_list.append(settings)
        thrust_list.append(thrust)

        if thrust > highest_thrust:
            highest_thrust = thrust
            highest_amp_settings = settings

    print(f'Highest thrust: {highest_thrust}')
    print(f'Amplifer Settings: {highest_amp_settings}')

        # for i in range(120):
        #     print(f'{amp_list[i]} __ {thrust_list[i]}')


        
        

def run(intcode, amp):
    amplifier = amp
    value = 0
    for num in amplifier:
        value = part1(intcode, num, value)

    return value




if __name__ in '__main__':
    solve()
