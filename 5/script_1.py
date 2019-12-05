OPT_QUIT = (99, 0)
OPT_SUM = (1, 4)
OPT_MUL = (2, 4)
OPT_IN  = (3, 1)
OPT_OUT = (4, 1)

INS_MOD = 0
CURSOR_STEP = 4

OPT_CODES = [OPT_SUM[0], OPT_MUL[0], OPT_IN[0], OPT_OUT[0]]

def read_input():
    values = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        values = [int(v) for v in line.split(",")]
    return values

def run_intcode(values:[]):
    cursor = 0
    opt_code = 0
    index_1 = 0
    index_2 = 0
    index_3 = 0
    result = 0

    while cursor < len(values):
        result = None
        opt_code = values[cursor]

        if(opt_code == OPT_QUIT or opt_code not in OPT_CODES):
            break

        if(opt_code == OPT_SUM[0]):
            index_1 = values[cursor + 1]
            index_2 = values[cursor + 2]
            index_3 = values[cursor + 3]

            value_1 = values[index_1]
            value_2 = values[index_2]

            result = value_1 + value_2

        if(opt_code == OPT_MUL[0]):
            index_1 = values[cursor + 1]
            index_2 = values[cursor + 2]
            index_3 = values[cursor + 3]

            value_1 = values[index_1]
            value_2 = values[index_2]

            result = value_1 * value_2

        if(opt_code == OPT_IN):
            result = int(input())

        if(opt_code == OPT_OUT):
            print(values[index_3], end='')

        values[index_3] = result
        cursor += CURSOR_STEP

x = 0
y = 0

with open("output.txt", "w+") as f:
    for i in range(99 + 1):
        for j in range(99 + 1):
            values = read_input()
            values[1] = i
            values[2] = j
            
            run_intcode(values)

            f.write(f"i: {i}, j: {j}\n")
            f.write(f"values: {values}\n")

            if values[0] == 19690720:
                print((i, j))
                x = i
                y = j
                
print(f"Result: {100 * x + y}")