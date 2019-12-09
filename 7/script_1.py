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

class Container():
    def __init__(self, amplifier, value):
        self.amplifier = amplifier
        self.value = value
        self.get_amplifier = True

    def set_amplifier(self, amplifier):
        self.amplifier = amplifier

    def set_value(self, value):
        #print(n1, end='') 
        self.value = value
        return WorkCode.DO_NOTHING

    def get_value(self):
        if self.get_amplifier:
            self.get_amplifier = False
            return self.amplifier
        self.get_amplifier = True
        return self.value

    def reset(self):
        self.value = 0
        self.amplifier = 0

def read_input():
    values = []
    with open('7/input.txt', 'r') as f:
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
    
    try:
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
    except:
        return None

    return values

def generate_amplifier_values(number):
    number_as_str = str(number).zfill(5)
    return [digit for digit in number_as_str]

def run_for_number(number, output_container, values):
    for amplifier in generate_amplifier_values(number):
        output_container.set_amplifier(int(amplifier))
        values = run_intcode(values, operations)
        if not values:
            return None
    power = output_container.value
    print(f"For input {number} power is {power}")
    output_container.reset()
    return power

if __name__ == "__main__":

    output_container = Container(0, 0)

    lambda_input = lambda: output_container.get_value()
    lambda_print = lambda n1: output_container.set_value(n1)

    OPT_QUIT = Operation(0, lambda: (WorkCode.DO_EXIT, None, 0))
    OPT_SUM = Operation(2, lambda n1, n2: (WorkCode.DO_SAVE, n1 + n2, 0))
    OPT_MUL = Operation(2, lambda n1, n2: (WorkCode.DO_SAVE, n1 * n2, 0))
    OPT_IN  = Operation(1, lambda n1: (WorkCode.DO_SAVE, lambda_input(), 0))
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

    run_for_number(43210, output_container, [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
    run_for_number(1234, output_container, [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])
    run_for_number(10423, output_container, [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])
    
    power = 0
    number = 0
    for i in range(44444 + 1):
        new_power = run_for_number(i, output_container, read_input())
        if new_power and power < new_power:
            power = new_power
            number = i

    print(f"Biggest power {power} for number {number}")