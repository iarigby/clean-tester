import os
import shutil
import zipfile


class FileManager:

    def __init__(self, root_dir, submission_name):
        self.root_dir: str = f"{root_dir}/{submission_name}"
        self.submission_name = submission_name

    def get_path(self, path, tmp=""):
        return f"{self.root_dir}{tmp}/{path}"

    # TODO have some general rule of where I call get_path here

    def clean_directory(self, directory):
        self.remove_directory(directory)
        os.makedirs(self.get_path(directory))

    def remove_directory(self, directory):
        p = self.get_path(directory)
        if os.path.exists(p):
            shutil.rmtree(p)

    def unzip_file(self, filename, unzip_path="", tmp=""):
        p = self.get_path(unzip_path, tmp)
        self.clean_directory(unzip_path+tmp)
        zip_ref = zipfile.ZipFile(filename+".zip", 'r')
        zip_ref.extractall(p)
        zip_ref.close()

    def get_list_of_zip(self, zip_path, tmp=""):
        submissions = []
        for file_name in os.listdir(self.get_path(zip_path, tmp)):
            if file_name.endswith("zip"):
                submissions.append(file_name[0:-4])
        return sorted(submissions, key=lambda x: x[0])
