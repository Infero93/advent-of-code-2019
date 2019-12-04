def read_input():
    instructions = []
    with open('input.txt', 'r') as f:
        for line in f:
            instructions.append([v.strip() for v in line.split(',')])
    return instructions

def unpack_instruction(instruction):
    return (instruction[0].lower(), int(instruction[1:]))

def calculate_new_point(point, instruction, length):
    x = point[0]
    y = point[1]

    if instruction == 'r':
        x += length
    elif instruction == 'l':
        x -= length
    elif instruction == 'u':
        y += length
    else:
        y -= length
    
    return (x,y)

def calculate_route(instructions):
    result = []
    sp = (0,0)
    np = None

    result.append(sp)
    for instruction in instructions:
        direction, length = unpack_instruction(instruction)
        for _ in range(length):
            np = calculate_new_point(sp, direction, 1)
            result.append(np)
            sp = np
    
    return result

instructions = read_input()
route_1 = calculate_route(instructions[0])
route_2 = calculate_route(instructions[1])
route_1_set = set(route_1)
route_2_set = set(route_2)

common = route_1_set.intersection(route_2_set)
common.remove((0,0))

distances = [route_1.index(p) + route_2.index(p) for p in common]
print(min(distances))