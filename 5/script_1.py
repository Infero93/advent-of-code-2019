class Operation():
    def __init__(self, operation, step):
        self.operation = operation
        self.step = step

    def __eq__(self, other):
        if isinstance(other, str):
            return self.operation == other
        elif isinstance(other, Operation):
            return self.operation == other.operation
        elif isinstance(other, int):
            if other > 9:
                return self.__eq__(str(other))
            return self.__eq__("0"+str(other))
        return False    

OPT_QUIT = Operation("99", 0)
OPT_SUM = Operation("01", 4)
OPT_MUL = Operation("02", 4)
OPT_IN  = Operation("03", 1)
OPT_OUT = Operation("04", 1)

INS_MOD = 0
CURSOR_STEP = 4

operations = [OPT_QUIT, OPT_SUM, OPT_MUL, OPT_IN, OPT_OUT]

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

        if(opt_code == OPT_QUIT or opt_code not in operations):
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

if __name__ == "__main__":
    opt_code = 1
    if(opt_code == OPT_QUIT or opt_code not in operations):
        print("NAY")
    else:
        print("OKAY")