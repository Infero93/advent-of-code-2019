from enum import Enum

class Operation():
    def __init__(self, params, func):
        self.params = params
        self.func = func

class WorkCode(Enum):
    NO_SAVE = 0
    DO_EXIT = 1

def lambda_print(n):
    print(n, end='') 
    return WorkCode.NO_SAVE

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
    
    with open('output.txt', 'w') as log_file:
        while cursor < len(values):
            params = []
            step = 1
            result = None

            instruction = create_instruction(values[cursor])
            opt_code = instruction[2:]
            opt_mode = instruction[:2]

            if(opt_code in operations):
                operation = operations[opt_code]

                if operation.params == 0:
                    result = operation.func()
                    step += 0
                elif operation.params == 1:
                    param1 = read_parameter(values, cursor + 1, opt_mode[1])
                    result = operation.func(param1)
                    step += 1
                    params.append(param1)
                elif operation.params == 2:
                    param1 = read_parameter(values, cursor + 1, opt_mode[1])
                    param2 = read_parameter(values, cursor + 2, opt_mode[0])
                    result = operation.func(param1, param2)
                    step += 3
                    params.append(param1)
                    params.append(param2)
            else:
                result = WorkCode.DO_EXIT

            if result == WorkCode.DO_EXIT:
                break

            if result != WorkCode.NO_SAVE:
                output_index = read_parameter(values, cursor + (step - 1), 1)

                log_file.write(f"Cursor: {cursor} | Step: {step} | Params: {params} | Full instruction: {instruction} | opt_mode: {opt_mode} | opt_code: {opt_code} | output_index: {output_index}\n")
                log_file.write(f"{values}\n")

                values[output_index] = result

            cursor += step
    
    return values

if __name__ == "__main__":

    OPT_QUIT = Operation(0, lambda: WorkCode.DO_EXIT)
    OPT_SUM = Operation(2, lambda n1, n2: n1 + n2)
    OPT_MUL = Operation(2, lambda n1, n2: n1 * n2)
    OPT_IN  = Operation(1, lambda n1: 1)
    OPT_OUT = Operation(1, lambda n1: lambda_print(n1))

    operations = {
        "99": OPT_QUIT,
        "01": OPT_SUM,
        "02": OPT_MUL,
        "03": OPT_IN,
        "04": OPT_OUT
    }

    values = read_input()
    print(len(values))
    values = run_intcode(values, operations)
    print()