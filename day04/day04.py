def part1(start, stop):
    count = 0
    for i in range(start, stop+1):
        if only_increasing(i) and contains_doubles(i):
            # print(i)
            count += 1

    return count

def part2(star, stop):
    count = 0
    for i in range(start, stop+1):
        if only_increasing(i) and contains_doubles(i):
            if isolated_double(i):
                count += 1
                # print(i)
    return count

def only_increasing(number):
    previous_num = ''
    for c in str(number):
        if len(previous_num) == 0: 
            previous_num = c
            continue
        
        if int(c) < int(previous_num):
            return False
    
        previous_num = c

    return True

def contains_doubles(number):
    number = str(number)

    if len(number) < 2:
        return False

    for i in range(0, len(number)-1):
        if number[i] is number[i+1]:
            return True 
    return False 

def ending_with_a_double(number):
    number = str(number)
    length = len(number)

    last_digit = number[length-1]
    second_last_digit = number[length-2]
    third_last_digit  = number[length-3]
    
    if last_digit == second_last_digit and second_last_digit != third_last_digit:
        return True
    return False

def isolated_double(number):
    number = str(number)
    length = len(number)
    atleast_one_double = False

    for x in range(0, length-1):
        if x == 0:
            if number[x] == number[x+1] and number[x+1] != number[x+2]:
                return True
        elif x+2 <= length-1:
            if number[x-1] != number[x] and number[x] == number[x+1] and number[x+1] != number[x+2]:
                return True
        elif x+1 <= length-1:
            if number[x-1] != number[x] and number[x] == number[x+1]:
                return True
        elif x <= length-1:
            if number[x-2] != number[x-1] and number[x-1] == number[x]:
                return True
        
    return False


if __name__ == '__main__':
    start = 138241
    stop  = 674034
    print(part1(start, stop))
    print(part2(start, stop))
