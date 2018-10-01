from logger import Logger
from helpers import make_call
from bcolors import *
import os
success_msg = OKGREEN + "success" + ENDC
fail_msg = FAIL + "failed" + ENDC

# TODO finish refactoring


class Tester:
    def __init__(self, work_path, filename, exe_name, f_input, f_output, student):
        self.work_path = work_path
        self.filename = filename
        self.exe_name = exe_name
        self.out_path = f"{self.work_path}/{self.exe_name}"
        self.f_output = f_output
        self.f_input = f_input
        self.student = student

    def run(self):
        output, err = make_call(f"clm -l -no-pie -nt -I {self.work_path} {self.filename} -o {self.out_path}")
        if os.path.exists(self.out_path):
            output, err = make_call(self.out_path)
            output = output.decode("utf-8")
            success = self.check_output(output, self.f_output)
            msg = fail_msg
            if success:
                msg = success_msg
            Logger.log(success, self.student)
            print(f"\t\t returned {msg} for input {self.f_input}")
        else:
            Logger.log(False, student=self.student, message="compile error")
            print("there was an error during compilation")

    @staticmethod
    def check_output(output, f_output):
        return output.strip() == str(f_output)