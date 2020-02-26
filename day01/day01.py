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
    sum = 0
    with open('input') as f: 
        for line in f: 
            sum += part1(int(line))
    print('Part 1: ' + sum)


if __name__ == '__main__':
    solve()