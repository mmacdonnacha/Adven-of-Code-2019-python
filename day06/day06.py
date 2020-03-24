def part1(list_of_orbits):
    orbits_dict = {}
    orbits_count = {'COM' : 0}

    orbits_dict = planet_orbit_dictionary(list_of_orbits)
    count = 0

    planet_list = list(orbits_dict.keys())
    
    while len(planet_list) > 0:
        for planet in planet_list:
            prev_planet = orbits_dict[planet]
            if prev_planet in orbits_count:
                current_planet_orbits = orbits_count[prev_planet] + 1
                count = count + current_planet_orbits
                orbits_count[planet] = current_planet_orbits

                planet_list.remove(planet)
            else:
                if orbits_dict[planet] is 'COM':
                    orbits_count[planet] = 1
                    planet_list.remove(planet)
    return count


def planet_orbit_dictionary(planet_list):
    orbits_dict = {}
    for planet in planet_list:
        orb = planet.split(')')
        if orb[1] in orbits_dict:
            orbits_dict[orb[1]] = orb[0]  # orbiting planet  -> center planet
        else:
            orbits_dict[orb[1]] = orb[0]
    return orbits_dict

def part2(list_of_orbits):
    orbits_dict = planet_orbit_dictionary(list_of_orbits)
    you_chain = orbiting_chain(orbits_dict, 'YOU')
    san_chain = orbiting_chain(orbits_dict, 'SAN')
    
    count = 0
    current_planet = ''
    for planet in you_chain:
        # print(planet)
        if planet in san_chain:
            current_planet = planet
            # count += 1
            break
        else:
            count += 1

    # print('============================================')

    index_current_planet = san_chain.index(current_planet)
    count += index_current_planet
    
    return count


def orbiting_chain(orbits_dictionary, planet):
    chain = []
    starting_planet = orbits_dictionary[planet]
    while orbits_dictionary[planet] != 'COM':
        planet = orbits_dictionary[planet]
        chain.append(planet)

    chain.append('COM')
    return chain


def solve():

    planet_list = []

    with open('input') as f: 
        for line in f: 
            planet_list.append(line.strip('\n'))
            
        part1_answer = part1(planet_list)
        print(f'Part1: {part1_answer}')

        part2_answer = part2(planet_list)
        print(f'Part2: {part2_answer}')


if __name__ == '__main__':
    # orbits = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']
    # part1(orbits)
    # print(part2(orbits))
    solve()
    