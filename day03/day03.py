
def part1(first_path, second_path):
    first_path_list  = [(0,0)]
    second_path_list = [(0,0)]
    
    for direction in first_path:
        first_path_list = update_path(first_path_list, direction)

    print('First path created')

    for direction in second_path:
        second_path_list = update_path(second_path_list, direction)

    print('Second path created')

    common_points = common_elements(first_path_list, second_path_list)

    print('Common points created')

    shortest_distance = 0
    for point in common_points:
        distance_from_origin = abs(point[0]) + abs(point[1])

        if distance_from_origin < shortest_distance or shortest_distance == 0:
            shortest_distance = distance_from_origin


    return shortest_distance


def update_path(direction_list, direction):
    arrow = direction[:1]
    length = int(direction[1:])
    starting_point = direction_list[-1]

    if arrow is 'R':
        for x in range(1, length+1):
            current_place = (starting_point[0] + x, starting_point[1])
            if current_place not in direction_list:
                direction_list.append(current_place)
            # print(current_place)
    
    if arrow is 'L':
        for x in range(1, length+1):
            current_place = (starting_point[0] - x, starting_point[1])
            if current_place not in direction_list:
                direction_list.append(current_place)
            # print(current_place)
            
    if arrow is 'U':
        for y in range(1, length+1):
            current_place = (starting_point[0], starting_point[1] + y)
            if current_place not in direction_list:
                direction_list.append(current_place)
            # print(current_place)

    if arrow is 'D':
        for y in range(1, length+1):
            current_place = (starting_point[0], starting_point[1] - y)
            if current_place not in direction_list:
                direction_list.append(current_place)
            # print(current_place)

    return direction_list


def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    result.remove((0,0))
    return result


def solve():
    
    paths = []

    with open('input') as f: 
        for line in f: 
            paths.append(line.strip('\n').split(','))
            
        part1_answer = part1(paths[0], paths[1])
        

    print(f'Part 1: {part1_answer}')
    # print(f'Part 1: {100 * part2_answer[0] + part2_answer[1]}')



if __name__ in '__main__':
    solve()
