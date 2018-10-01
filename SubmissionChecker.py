from FileManager import FileManager
from FunctionData import FunctionData
from Config import Config
from SubmissionData import SubmissionData


class SubmissionChecker:

    def __init__(self, submission_data: SubmissionData, config: Config):
        self.submission_name: str = submission_data.name
        self.submission_file_name = submission_data.file_name
        self.functions_data: FunctionData = submission_data.functions
        self.test_directory = config.test_directory
        self.exe_filename = config.exe_filename
        self.file_manager = FileManager('submission-checker/', self.submission_name)
        self.students_list: list = []

    def initialize(self):
        print("cleaning files from last session...")
        # self.file_manager.clean_directory(self.test_directory)

    def clean_up(self):
        self.file_manager.remove_directory(self.test_directory)

    def start_session(self):
        self.initialize()
        self.file_manager.unzip_all_files(self.submission_name, tmp="/tmp", testdir=self.test_directory)
        self.students_list = self.file_manager.get_list_of_zip(self.submission_name, "/tmp")
        for student in self.students_list:
            self.evaluate_submission(student)

    def evaluate_submission(self, student):
        print("\n\n*** checking student " + student)
        self.submission_name = ""
