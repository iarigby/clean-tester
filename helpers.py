import json
from collections import namedtuple
import subprocess

def get_test_data(json_filename):
    with open(json_filename, "r") as rf:
        return json.loads(rf.read(), object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


def make_call(command):
    return subprocess.check_output(command.split(" ")).decode("utf-8")
