from datetime import datetime
from typing import List
import re
from enum import Enum, auto


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


class Student:

    def __init__(self, string):
        pattern = r"([\w+\s]*)\(([a-zA-Z0-9]{6})\)"
        m = re.match(pattern, string)
        self.name = m.group(1)
        self.code = m.group(2)
        self.group = 0


class Evaluation(Enum):
    NOT_EVALUATED = auto()
    ACCEPTED = auto()
    REJECTED = auto()


class Submission:

    def __init__(self, student: Student, functions: List[FunctionData], content="", evaluation=Evaluation.NOT_EVALUATED):
        self.nept_code = student.code
        self.file_content = content
        self.processed = None
        self.content = None
        self.evaluated = False
        self.evaluation = evaluation
        self.comments = "\tcomments:\n"
        self.results = {func.name: {f_input: "" for f_input in func.tests} for func in functions}

        # TODO
    def process_content(self):
        self.content = ""
        # remove start expressions
        # if function exists,

    # this can be used for renameing
    def change_functions(self):
        for func in self.results.keys():
            # if exists, write as is
            # rename parameters (not a trivial task, because of pattern matching and stuff)
            # if not, ask user for input
            print()

    def add_comment(self, comment):
        self.comments = self.comments + comment








































































































































class Session:

    def __init__(self, task, students: List[Student], functions: List[FunctionData], ):
        self.task = task
        self.students = students
        self.functions = functions
        self.submissions = [Submission(student, functions) for student in students]


class SubmissionData:

    def __init__(self, name, file_name, functions: FunctionData):
        self.name = name
        self.file_name = file_name
        self.functions: List[FunctionData] = functions


class Results:

    def __init__(self, hw, submissions: List[Submission]):
        t = datetime.now()
        self.start_time = f"{t.day}_{t.month}_{t.year}_{t.hour}_{t.minute}"
        # self.results =
        # TODO


class Result:

    def __init__(self, student):
        print()
        # TODO
