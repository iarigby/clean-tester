import os
import shutil
import zipfile
from logger import *
from pathManager import PathManager


class FileManager:

    def __init__(self, path_manager: PathManager):
        self.path_mgr = path_manager
        self.students_list = []
        self.input_handler = InputHandler(True) # TODO move this somewhere else

    def clean_directory(self, directory):
        self.remove_directory(directory)
        os.makedirs(directory)

    @staticmethod
    def remove_directory(directory):
        if os.path.exists(directory):
            shutil.rmtree(directory)

    def unzip_all_files(self, confirm):
        unzip_path = self.path_mgr.get_first_unzip_path()
        self.clean_directory(unzip_path)
        self.unzip(self.path_mgr.get_first_zip_path(), unzip_path)
        self.students_list = self.get_students_list()
        if confirm(Confirmations.UNZIP_MAIN_FILE):
            # TODO ugh this part makes me wanna puke
            for student in self.students_list:
                path = self.path_mgr.get_student_zip_path(student)
                student_unzip_path = self.path_mgr.get_student_unzip_path(student)
                if not os.path.exists(student_unzip_path):
                    os.makedirs(student_unzip_path)
                    # TODO moved these in if statement, decide how to implement finally
                    self.unzip(path, student_unzip_path)
                    self.rename_file(student_unzip_path)
        else:
            with open("list.txt", "r") as stlist:
                self.students_list = stlist.read().split("\n")
                print(self.students_list)
                confirm(Confirmations.CONTINUE)
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

    def create_test_dir(self, student):
        self.clean_directory(self.path_mgr.get_test_path(student))

    def get_file_content(self, student, filename):
        try:
            with open(f"{self.path_mgr.get_student_unzip_path(student)}/{filename}.icl", "r") as read_file:
                contents = read_file.read()
                contents = contents.replace("\n Start", "//Start")
                contents = contents.replace("\nStart", "//Start")
                return contents
        except FileNotFoundError:
            log(False, student, "could not find file " + filename)
            return False

    def rename_file(self, path):
        contents = os.listdir(path)
        if len(contents) > 1 and not self.path_mgr.test_dir in contents:
                print("there are multiple files in " + path)
                input("waiting for you to resolve thism press enter to continue...")
        for file in os.listdir(path):
            if file.endswith(".icl"):
                os.rename(f"{path}/{file}", f"{path}/{self.path_mgr.file_name}.icl")
