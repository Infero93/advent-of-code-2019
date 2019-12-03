def draw_lines(line, max_x = 100, max_y = 100, start_x = None, start_y = None):
    area = [[]]

    for y in range(max_x):
        area.append(['.']*max_y)

    if not start_x:
        start_x = (max_x // 2) - 1

    if not start_y:
        start_y = (max_y // 2) - 1

    area[start_x][start_y] = 'o'

    next_x = start_x
    next_y = start_y

    instructions = [inst.strip() for inst in line.split(',')]
    for instruction in instructions:
        print(f"Next coordinate: {(next_x, next_y)}")
        direction = instruction[0].lower()
        length = int(instruction[1:])

        if direction is 'r':
            next_x += length
        elif direction is 'l':
            next_x -= length
        elif direction is 'u':
            next_y += length
        else:
            next_y -= length

        try:
            area[next_x][next_y] = 'x'
        except IndexError:
            print(f"Instruction out of index: {instruction}")

    return area

result = ""

index = 0
with open('input.txt', 'r') as f:
    for line in f:
        area = draw_lines(line, 11, 10, 1, 8)
        with open(f'output{index}.txt', 'w') as ff:
            for index in range(len(area)):
                ff.write("".join(area[index]) + "\n")

        index += 1