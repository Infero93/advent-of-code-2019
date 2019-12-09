from enum import Enum, auto

class Operation():
    def __init__(self, params, func):
        self.params = params
        self.func = func

class WorkCode(Enum):
    DO_EXIT = auto()
    DO_NOTHING = auto()
    DO_INCREASE = auto()
    DO_SAVE = auto()
    DO_JUMP = auto()

def lambda_print(n):
    print(n, end='') 
    return WorkCode.DO_NOTHING

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
    mode = int(mode)

    if mode == 1:
        return values[cursor]

    return values[values[cursor]]

def run_intcode(values:[], operations):
    cursor = 0
    opt_code = 0
    result = 0
    
    while cursor < len(values):
        step = 1
        result = None
        work_code = WorkCode.DO_EXIT
        step_modifier = 0

        instruction = create_instruction(values[cursor])
        opt_code = instruction[2:]
        opt_mode = instruction[:2]

        if(opt_code in operations):
            operation = operations[opt_code]

            if operation.params == 0:
                work_code, result, step_modifier = operation.func()
                step += 0
            elif operation.params == 1:
                param1 = read_parameter(values, cursor + 1, opt_mode[1])
                work_code, result, step_modifier = operation.func(param1)
                step += 1
            elif operation.params == 2:
                param1 = read_parameter(values, cursor + 1, opt_mode[1])
                param2 = read_parameter(values, cursor + 2, opt_mode[0])
                work_code, result, step_modifier = operation.func(param1, param2)
                step += 3

        if work_code == WorkCode.DO_EXIT:
            break

        if work_code == WorkCode.DO_SAVE:
            output_index = read_parameter(values, cursor + (step - 1), 1)
            values[output_index] = result

        if work_code == WorkCode.DO_JUMP:
            cursor = result
        else:
            step += step_modifier
            cursor += step
    
    return values

if __name__ == "__main__":

    OPT_QUIT = Operation(0, lambda: (WorkCode.DO_EXIT, None, 0))
    OPT_SUM = Operation(2, lambda n1, n2: (WorkCode.DO_SAVE, n1 + n2, 0))
    OPT_MUL = Operation(2, lambda n1, n2: (WorkCode.DO_SAVE, n1 * n2, 0))
    OPT_IN  = Operation(1, lambda n1: (WorkCode.DO_SAVE, 5, 0))#int(input())))
    OPT_OUT = Operation(1, lambda n1: (WorkCode.DO_INCREASE, lambda_print(n1), 0))
    OPT_JIT = Operation(2, lambda n1, n2: (WorkCode.DO_JUMP if n1 != 0 else WorkCode.DO_NOTHING, n2 if n1 != 0 else None, -1))
    OPT_JIF = Operation(2, lambda n1, n2: (WorkCode.DO_JUMP if n1 == 0 else WorkCode.DO_NOTHING, n2 if n1 == 0 else None, -1))
    OPT_LT  = Operation(2, lambda n1, n2: (WorkCode.DO_SAVE, 1 if n1 < n2 else 0, 0))
    OPT_EQ  = Operation(2, lambda n1, n2: (WorkCode.DO_SAVE, 1 if n1 == n2 else 0, 0))

    operations = {
        "99": OPT_QUIT,
        "01": OPT_SUM,
        "02": OPT_MUL,
        "03": OPT_IN,
        "04": OPT_OUT,
        "05": OPT_JIT,
        "06": OPT_JIF,
        "07": OPT_LT,
        "08": OPT_EQ
    }

    values = read_input()
    values = run_intcode(values, operations)
    print()