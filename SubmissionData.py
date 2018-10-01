from FunctionData import FunctionData


class SubmissionData:
    functions: FunctionData

    def __init__(self, name, file_name, functions: FunctionData):
        self.name = name
        self.file_name = file_name
        self.functions = functions
