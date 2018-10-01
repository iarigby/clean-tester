from typing import List


class Test:

    def __init__(self, f_input, expected_output, hidden=False):
        self.f_input = f_input
        self.expected_output = expected_output
        self.hidden: bool = hidden


class FunctionData:

    def __init__(self, name, description, tests: List[Test]):
        self.name = name
        self.description = description
        self.tests: List[Test] = tests


class SubmissionData:

    def __init__(self, name, file_name, functions: FunctionData):
        self.name = name
        self.file_name = file_name
        self.functions: List[FunctionData] = functions
