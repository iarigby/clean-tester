import os
import shutil
import zipfile


class FileManager:

    def __init__(self, root_dir, submission_name):
        self.root_dir: str = f"./{root_dir}/{submission_name}"
        self.submission_name = submission_name

    def get_path(self, path: str, tmp=""):
        if path.startswith(self.root_dir):
            return f"{tmp}/{path}"
        return f"{self.root_dir}{tmp}/{path}"

    # TODO have some general rule of where I call get_path here

    def clean_directory(self, directory):
        p = self.get_path(directory)
        self.remove_directory(p)
        os.makedirs(p)

    def remove_directory(self, directory):
        p = self.get_path(directory)
        print(p)
        if os.path.exists(p):
            shutil.rmtree(p)
            os.removedirs(p)

    def unzip_all_files(self, filename, unzip_path="", tmp="", testdir=""):
        p = self.get_path(unzip_path, tmp)
        # self.clean_directory(p)
        self.unzip(filename, p)
        unzipped_location = p + "/" + self.submission_name
        zip_list = self.get_list_of_zip(self.submission_name, tmp)
        print(zip_list)
        for file in zip_list:
            path = f"{unzipped_location}/{file}"
            unzip_path = f"{self.get_path(testdir)}/{file}"
            os.makedirs(unzip_path)
            self.unzip(path, unzip_path)

    def unzip(self, filename, unzip_path):
        print("extracting " + filename + " to " + unzip_path)
        zip_ref = zipfile.ZipFile(filename + ".zip", 'r')
        zip_ref.extractall(unzip_path)
        zip_ref.close()

    def get_list_of_zip(self, zip_path, tmp=""):
        submissions = []
        for file_name in os.listdir(self.get_path(zip_path, tmp)):
            if file_name.endswith("zip"):
                submissions.append(file_name[0:-4])
        return sorted(submissions, key=lambda x: x[0])
