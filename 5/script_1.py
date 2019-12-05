class Operation():
    def __init__(self, params, step, func):
        self.params = params
        self.step = step
        self.func = func

def lambda_print(n):
    print(n, end='') 
    return n

# INS_MOD = 0
# CURSOR_STEP = 4

# operations = [OPT_QUIT, OPT_SUM, OPT_MUL, OPT_IN, OPT_OUT]


# def read_input():
#     values = []
#     with open('input.txt', 'r') as f:
#         line = f.readline()
#         values = [int(v) for v in line.split(",")]
#     return values

def run_intcode(values:[], operations):
    cursor = 0
    opt_code = 0
    index_1 = 0
    index_2 = 0
    index_3 = 0
    result = 0

    while cursor < len(values):
        result = None

        instruction = create_instruction(values[cursor])
        opt_code = instruction[2:]
        opt_mode = instruction[:2]

        if(opt_code not in operations):
            break

        operation = operations[opt_code]

        if operation.params == 0:
            result = operation.func()
        elif operation.params == 1:
            param1 = read_parameter(values, cursor + 1, opt_mode[1])
            result = operation.func(param1)
        elif operation.params == 2:
            param1 = read_parameter(values, cursor + 1, opt_mode[1])
            param2 = read_parameter(values, cursor + 2, opt_mode[0])
            result = operation.func(param1, param2)


        if result == None:
            break

        cursor += operation.step

        # if(opt_code == OPT_SUM[0]):
        #     index_1 = values[cursor + 1]
        #     index_2 = values[cursor + 2]
        #     index_3 = values[cursor + 3]

        #     value_1 = values[index_1]
        #     value_2 = values[index_2]

        #     result = value_1 + value_2

        # if(opt_code == OPT_MUL[0]):
        #     index_1 = values[cursor + 1]
        #     index_2 = values[cursor + 2]
        #     index_3 = values[cursor + 3]

        #     value_1 = values[index_1]
        #     value_2 = values[index_2]

        #     result = value_1 * value_2

        # if(opt_code == OPT_IN):
        #     result = int(input())

        # if(opt_code == OPT_OUT):
        #     print(values[index_3], end='')

        # values[index_3] = result
        # cursor += CURSOR_STEP

def create_instruction(value):
    value_as_str = str(value)
    if len(value_as_str) < 4:
        return value_as_str.zfill(4)
    return value_as_str

def read_parameter(values, cursor, mode):
    index = None

    if mode == 0:
        index = values[cursor]
    else:
        index = cursor

    return values[index]

if __name__ == "__main__":

    OPT_QUIT = Operation(0, 0, lambda: None)
    OPT_SUM = Operation(2, 4, lambda n1, n2: n1 + n2)
    OPT_MUL = Operation(2, 4, lambda n1, n2: n1 * n2)
    OPT_IN  = Operation(0, 1, lambda: input())
    OPT_OUT = Operation(1, 1, lambda n1: lambda_print(n1))

    operations = {
        "99": OPT_QUIT,
        "01": OPT_SUM,
        "02": OPT_MUL,
        "03": OPT_IN,
        "04": OPT_OUT
    }


    print()

    # print(create_instruction(1))
    # print(create_instruction(11))
    # print(create_instruction(111))
    # print(create_instruction(1111))
    # print(operations["99"])
    # opt_code = 1
    # if(opt_code == OPT_QUIT or opt_code not in operations):
    #     print("NAY")
    # else:
    #     print("OKAY")