def draw_lines(line, max_x = 100, max_y = 100, start_x = None, start_y = None, area = None):
    if not area:
        area = [[]]

        for y in range(max_x):
            area.insert(y, ['.']*max_y)

    if not start_x and start_x is not 0:
        start_x = (max_x // 2) - 1

    if not start_y and start_y is not 0:
        start_y = (max_y // 2) - 1

    area[start_y][start_x] = 'o'

    next_x = start_x
    next_y = start_y

    instructions = [inst.strip() for inst in line.split(',')]
    for instruction in instructions:
        direction = instruction[0].lower()
        length = int(instruction[1:]) - 1

        if direction == 'r':
            next_x += length
        elif direction == 'l':
            next_x -= length
        elif direction == 'u':
            next_y -= length
        else:
            next_y += length

        while next_x > start_x:
            area[start_y][start_x + 1] = '-'
            start_x += 1
        
        while next_x < start_x:
            area[start_y][start_x - 1] = '-'
            start_x -= 1

        while next_y > start_y:
            area[start_y + 1][start_x] = '|'
            start_y += 1

        while next_y < start_y:
            area[start_y - 1][start_x] = '|'
            start_y -= 1    

        try:
            print(f"Next coordinate: {(next_x, next_y)}")
            area[next_y][next_x] = '+'
        except IndexError:
            print(f"Instruction out of index: {instruction}")

    return area

index = 0
with open('input.txt', 'r') as f:
    area = None

    for line in f:
        area = draw_lines(line, 250, 400, None, None, area)

    with open(f'output.txt', 'w') as ff:
        for index in range(len(area)):
            ff.write("".join(area[index]) + "\n")

    index += 1