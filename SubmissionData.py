from FunctionData import FunctionData
from typing import List


class SubmissionData:

    def __init__(self, name, file_name, functions: FunctionData):
        self.name = name
        self.file_name = file_name
        self.functions: List[FunctionData] = functions
