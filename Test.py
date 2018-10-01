class Test:

    def __init__(self, f_input, expected_output, hidden=False):
        self.f_input = f_input
        self.expected_output = expected_output
        self.hidden: bool = hidden
