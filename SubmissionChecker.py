from Tester import Tester

from FileManager import FileManager
from FunctionData import FunctionData
from Config import Config
from PathManager import PathManager
from SubmissionData import SubmissionData
from subprocess import CalledProcessError
from typing import List
from bcolors import *


class SubmissionChecker:

    def __init__(self, submission_data: SubmissionData, config: Config):
        self.submission_name: str = submission_data.name
        self.filename = submission_data.file_name  # TODO remove this dependency
        self.exe_name = config.exe_filename
        self.functions_data: List[FunctionData] = submission_data.functions
        self.path_manager = PathManager("submission-checker", submission_data, config)
        self.file_manager = FileManager(self.path_manager)

    def start_session(self):
        self.file_manager.unzip_all_files()
        for student in self.file_manager.students_list:
            self.evaluate_submission(student)

    def evaluate_submission(self, student):
        print("\n\n*** checking submission from " + student)
        for func in self.functions_data:
            self.run_tests(student, func)

    def run_tests(self, student, func):
        print(f"*** {OKBLUE}testing function {func.name} {ENDC}***")
        for test in func.tests:
            # TODO test.f_input instead of test.input
            self.create_test_file(student, func.name, test.input)
            try:
                # TODO finish refactoring this part
                tester = Tester(self.path_manager.get_test_path(student),
                                self.filename, self.exe_name,
                                test.input, test.output, student)
                tester.run()

            except CalledProcessError:
                print("check this out")

    def create_test_file(self, student, clean_func, args):
        out_path = self.path_manager.get_test_path(student)
        in_path = self.path_manager.get_student_unzip_path(student)
        self.file_manager.clean_directory(out_path)
        with open(f'{out_path}/{self.filename}.icl', 'w+') as testfile:
            contents = self.get_file_content(in_path)
            testfile.write(contents)
            testfile.write(f"\nStart = {clean_func} {args}")

    def get_file_content(self, path):
        try:
            with open(f"{path}/{self.filename}.icl", "r") as read_file:
                contents = read_file.read()
                contents = contents.replace("\n Start", "//Start")
                contents = contents.replace("\nStart", "//Start")
                return contents
        except FileNotFoundError:
            return ""
