class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{(self.x, self.y)}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# def check_if_intersect(a1, a2, b1, b2):
#     line1 = LineString([(a1.x, a1.y), (a2.x, a2.y)])
#     line2 = LineString([(b1.x, b1.y), (b2.x, b2.y)])
#     inter = line1.intersection(line2)

#     if inter.is_empty:
#         return None

#     return Point(inter.x, inter.y)

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

def caluculate_route(instructions):
    result = []
    sp = (0,0)
    np = None

    result.append(sp)
    for instruction in instructions:
        direction, length = unpack_instruction(instruction)
        for i in range(length):
            np = calculate_new_point(sp, direction, 1)
            result.append(np)
            sp = np
    
    return set(result)

instructions = read_input()
route_1_set = caluculate_route(instructions[0])
route_2_set = caluculate_route(instructions[1])
common = route_1_set.intersection(route_2_set)
common.remove((0,0))

#print(route_1_set)
#print(route_2_set)
#print(common)

distances = [abs(p[0]) + abs(p[1]) for p in common]
print(distances)
print(min(distances))

# instructions_1_sp = Point(0,0)
# instructions_2_sp = Point(0,0)
# instructions_1_pp = Point(0,0)
# instructions_1_np = Point(0,0)
# instructions_2_pp = Point(0,0)
# instructions_2_np = Point(0,0)

# intersections = []

# for instruction_1 in instructions[0]:
#     direction, length = unpack_instruction(instruction_1)

# for instruction_1 in instructions[0]:
#     direction_1, length_1 = unpack_instruction(instruction_1)
#     instructions_1_np = calculate_new_point(instructions_1_pp, direction_1, length_1)

#     for instruction_2 in instructions[1]:
#         direction_2, length_2 = unpack_instruction(instruction_2)
#         instructions_2_np = calculate_new_point(instructions_2_np, direction_2, length_2)

#         #print(f"Point 1-1: {instructions_1_pp}")
#         #print(f"Point 1-2: {instructions_1_np}")
#         #print(f"Point 2-1: {instructions_2_pp}")
#         #print(f"Point 2-2: {instructions_2_np}")

#         inter = check_if_intersect(instructions_1_pp, instructions_1_np, instructions_2_pp, instructions_2_np)
#         if inter and not (inter.x == inter.y and inter.x == 0):
#             intersections.append(inter)

#         instructions_2_pp = instructions_2_np

#     instructions_1_pp = instructions_1_np
#     instructions_2_np = instructions_2_sp

# distances = [abs(p.x) + abs(p.y) for p in intersections]
# print(intersections)
# print(distances)
# print(min(distances))