class Operation():
    def __init__(self, params, step, func):
        self.params = params
        self.step = step
        self.func = func

def lambda_print(n):
    print(n, end='') 
    return n

def read_input():
    values = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        values = [int(v) for v in line.split(",")]
    return values

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

def run_intcode(values:[], operations):
    cursor = 0
    opt_code = 0
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

        output_index = read_parameter(values, operation.step - 1, 1)
        values[output_index] = result
        cursor += operation.step

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


    print(read_parameter([0,3,5], 1, 0))