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


def solve():
    part1_answer = 0
    planet_list = []

    with open('input') as f: 
        for line in f: 
            planet_list.append(line.strip('\n'))
            
        part1_answer = part1(planet_list)
        print(part1_answer)


if __name__ == '__main__':
    # orbits = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
    # part1(orbits)
    # print(part1(orbits))
    solve()
    