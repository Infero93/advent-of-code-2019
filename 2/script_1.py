OPT_QUIT = 99
OPT_SUM = 1
OPT_MUL = 2
CURSOR_STEP = 4

values = []
with open('input.txt', 'r') as f:
    line = f.readline()
    values = [int(v) for v in line.split(",")]

values[1] = 12
values[2] = 2

cursor = 0
opt_code = 0
index_1 = 0
index_2 = 0
index_3 = 0
result = 0

while cursor < len(values):
    opt_code = values[cursor]

    if(opt_code == OPT_QUIT or not (opt_code == OPT_SUM or opt_code == OPT_MUL)):
        break

    index_1 = values[cursor + 1]
    index_2 = values[cursor + 2]
    index_3 = values[cursor + 3]

    value_1 = values[index_1]
    value_2 = values[index_2]

    if(opt_code == OPT_SUM):
        values[index_3] = value_1 + value_2

    if(opt_code == OPT_MUL):
        values[index_3] = value_1 * value_2

    cursor += CURSOR_STEP

print(values[0])