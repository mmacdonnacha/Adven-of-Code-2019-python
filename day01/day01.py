from math import floor

def part1(mass):
    return floor(mass / 3) - 2


def part2(mass):
    total_fuel = 0
    while mass >= 0:
        mass = part1(mass)
        if mass >=  0:
            total_fuel += mass

    return total_fuel


def solve():
    part1_sum = 0
    part2_sum = 0

    with open('input') as f: 
        for line in f: 
            num = int(line)
            part1_sum += part1(num)
            part2_sum += part2(num)
    print('Part 1: ' + str(part1_sum))
    print('Part 2: ' + str(part2_sum))


if __name__ == '__main__':
    solve()