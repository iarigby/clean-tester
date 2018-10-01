from config import Config
from dataReprs import SubmissionData


class PathManager:
    def __init__(self, root_dir, submission: SubmissionData, config: Config):
        self.submission_name = submission.name
        self.root_dir: str = f"./{root_dir}/{self.submission_name}"
        self.file_name = submission.file_name
        self.test_dir = config.test_dir
        self.source_dir = config.source_dir
        self.zip_path = config.zip_dir

    def path_from_root(self, directory):
        return f"{self.root_dir}/{directory}"

    def get_test_path(self, student):
        return f"{self.get_student_unzip_path(student)}/{self.test_dir}"

    def get_source_path(self):
        return self.path_from_root(self.source_dir)

    def get_student_unzip_path(self, student):
        student_dir = student.replace(" ", "")
        return f"{self.get_source_path()}/{student_dir}"

    def get_student_zip_path(self, student):
        return f"{self.get_students_zip_path()}/{student}.zip"

    def get_students_zip_path(self):
        return f"{self.get_first_unzip_path()}/{self.submission_name}"

    def get_first_zip_path(self):
        return f"{self.zip_path}/{self.submission_name}.zip"

    def get_first_unzip_path(self):
        return self.path_from_root("tmp")


