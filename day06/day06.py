def part1(list_of_orbits):
    orbits_dict = {}
    orbits_count = {'COM' : 0}

    orbits_dict = planet_orbit_dictionary(list_of_orbits)
    # print(orbits_dict)
    count = 0

    planet_list = list(orbits_dict.keys())
    # for planet in planet_list:
    #     prev_planet = orbits_dict[planet]
    #     if orbits_dict[planet] in orbits_count:
    #         current_planet_orbits = orbits_count[prev_planet] + 1
    #         count = count + current_planet_orbits
    #         orbits_count[planet] = current_planet_orbits
    #     # print(f'{orbits_dict[planet]} is orbited by {planet}')
    #     else:
    #         if orbits_dict[planet] is 'COM':

    #             orbits_count[planet] = 1
    #         else:
    #             orbits_count[planet] = orbits_count[prev_planet]+ 1

    while len(planet_list) > 0:
        for planet in planet_list:
            prev_planet = orbits_dict[planet]
            if prev_planet in orbits_count:
                current_planet_orbits = orbits_count[prev_planet] + 1
                count = count + current_planet_orbits
                orbits_count[planet] = current_planet_orbits

                planet_list.remove(planet)
            # print(f'{orbits_dict[planet]} is orbited by {planet}')
            else:
                if orbits_dict[planet] is 'COM':
                    orbits_count[planet] = 1
                    planet_list.remove(planet)
        
        # print('-------------------------------------------')
        # print('-------------------------------------------')
        # print('-------------------------------------------')
        # print(planet_list)



        
        # a)b     value)key

    # for x in orbits_dict.keys():
    #     print(f'{orbits_dict[x]} is orbited by {x}')
    # print(len(orbits_dict.keys()))

    return count

    

# loop through planet list until you find 'COM'
# add it to orbit_dict and remove from planet_list
# keep looping until plant_list is empty
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
            # print(line.strip('\n'))
            planet_list.append(line.strip('\n'))
            
        # part1_list = list.copy(intcode)
        # print(planet_list)
        # print(len(planet_list))
        part1_answer = part1(planet_list)
        print(part1_answer)


if __name__ == '__main__':
    # orbits = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
    # part1(orbits)
    # print(part1(orbits))
    print(solve())
    # print('doing nothing right now')