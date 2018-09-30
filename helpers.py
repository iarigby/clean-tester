import json
from collections import namedtuple
import subprocess
import zipfile


def unzip_file(filename, unzip_path=""):
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall(unzip_path)
    zip_ref.close()


def get_file_content(filename):
    with open(f"{filename}.icl", "r") as read_file:
        contents = read_file.read()
        contents = contents.replace("\n Start", "//Start")
        contents = contents.replace("\nStart", "//Start")
        return contents


def get_test_data(json_filename):
    with open(json_filename, "r") as rf:
        return json.loads(rf.read(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


def make_call(command):
    return subprocess.Popen(command.split(" "), stdout=subprocess.PIPE).communicate()
