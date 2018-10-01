import os
import shutil
import zipfile

from PathManager import PathManager


class FileManager:

    def __init__(self, path_manager: PathManager):
        self.path_mgr = path_manager
        self.students_list = []

    def clean_directory(self, directory):
        self.remove_directory(directory)
        os.makedirs(directory)

    @staticmethod
    def remove_directory(directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)

    def unzip_all_files(self):
        unzip_path = self.path_mgr.get_first_unzip_path()
        self.clean_directory(unzip_path)
        self.unzip(self.path_mgr.get_first_zip_path(), unzip_path)
        self.students_list = self.get_students_list()
        for student in self.students_list:
            path = self.path_mgr.get_student_zip_path(student)
            student_unzip_path = self.path_mgr.get_student_unzip_path(student)
            if not os.path.exists(student_unzip_path):
                os.makedirs(student_unzip_path)
            self.unzip(path, student_unzip_path)
        self.clean_directory(unzip_path)

    @staticmethod
    def unzip(p_from, p_to):
        zip_ref = zipfile.ZipFile(p_from, 'r')
        zip_ref.extractall(p_to)
        zip_ref.close()

    def get_students_list(self):
        submissions = []
        for file_name in os.listdir(self.path_mgr.get_students_zip_path()):
            if file_name.endswith("zip"):
                submissions.append(file_name[0:-4])
        return sorted(submissions, key=lambda x: x[0])
