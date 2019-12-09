class Operation():
    def __init__(self, func):
        self.func = func

    def run(self, cursor, values):
        pass

    def __build_instruction(self, value):
        value_as_str = str(value)
        return value_as_str.zfill(4)

    def __read_parameter(self, mode, values, pointer):
        mode = int(mode)
        if mode == 1:
            return values[pointer]

        return values[values[pointer]]

    pass