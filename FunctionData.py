from Test import Test
from typing import List


class FunctionData:

    def __init__(self, name, description, tests: List[Test]):
        self.name = name
        self.description = description
        self.tests: List[Test] = tests
