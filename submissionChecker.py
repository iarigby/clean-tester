from subprocess import CalledProcessError
from typing import List

from bcolors import *
from config import Config
from dataReprs import FunctionData, SubmissionData
from fileManager import FileManager
from pathManager import PathManager
from tester import Tester
from logger import *


class SubmissionChecker:

    def __init__(self, submission_data: SubmissionData, config: Config):
        self.submission_name: str = submission_data.name
        self.filename = submission_data.file_name  # TODO remove this dependency
        self.exe_name = config.exe_filename
        self.functions_data: List[FunctionData] = submission_data.functions
        self.path_manager = PathManager("submission-checker", submission_data, config)
        self.file_manager = FileManager(self.path_manager)
        self.input_handler = InputHandler(True)

    def start_session(self):
        self.file_manager.unzip_all_files(self.confirm)
        for student in self.file_manager.students_list:
            self.file_manager.create_test_dir(student)
            self.evaluate_submission(student)

    def evaluate_submission(self, student):
        content = self.file_manager.get_file_content(student, self.filename)
        if content:
            tester = Tester(self.path_manager.get_test_path(student),
                            self.filename, self.exe_name, student,
                            content)
            res = True
            while res:
                print("\n\n*** checking submission from " + student)
                write_message(student)
                # TODO EW next two lines
                content = self.file_manager.get_file_content(student, self.filename)
                tester.reload_content(content)
                print(tester.content)
                for func in self.functions_data:
                    self.run_tests(tester, func)
                res = self.confirm(Confirmations.RECHECK_SUBMISSION)

    def run_tests(self, tester: Tester, func):
        print(f"*** {OKBLUE}testing function {func.name} {ENDC}***")
        write_message("\t" + func.name)
        tester.change_function(func.name)
        for test in func.tests:
            # TODO test.f_input instead of test.input
            try:
                tester.run(test.input, test.output)
            except CalledProcessError:
                print("check this out")
        comment = self.confirm(Confirmations.ADDITIONAL_COMMENTS)
        if comment:
            write_message(comment)

    def confirm(self, confirmation):
        return self.input_handler.confirm(confirmation)
