from logger import *
from helpers import make_call
from bcolors import *
import os
import re

success_msg = OKGREEN + "success" + ENDC
fail_msg = FAIL + "failed" + ENDC

# TODO finish refactoring


class Tester:
    def __init__(self, work_path, filename, exe_name, student, content):
        self.work_path = work_path
        self.filename = filename
        self.exe_name = exe_name
        self.out_path = f"{self.work_path}/{self.exe_name}"
        self.student = student
        self.content: str = self.load_content(content)
        self.func_name = ""
        self.compiles = True

    def run(self, f_input, f_output):
        if self.compiles:
            self.create_test_file(f_input)
            output, err = make_call(f"clm -l -no-pie -nt -I {self.work_path} {self.filename} -o {self.out_path}")
            if err:
                self.compiles = False
            if not err and os.path.exists(self.out_path):
                output, err = make_call(self.out_path)
                output = output.decode("utf-8")
                success = self.check_output(output, f_output)
                msg = fail_msg
                if success:
                    msg = success_msg
                write_message(f"\t{f_input}: {str(success)},", )
                print(f"\t\t returned {msg} for input {f_input}")
            else:
                write_message("compile error")

    def load_content(self, content):
        pattern = re.compile("module [a-zA-Z0-9_]+[ ]*\n")
        return re.sub(pattern, f"module {self.filename}\n", content)

    def reload_content(self, content):
        self.content = self.load_content(content)

    @staticmethod
    def check_output(output, f_output):
        return output.strip() == str(f_output)

    def create_test_file(self, args):
        # self.file_manager.clean_directory(out_path)
        # TODO not sure if above line is necessary, check when it's not past 1am x_x
        with open(f'{self.work_path}/{self.filename}.icl', 'w+') as testfile:
            testfile.write(self.content)
            testfile.write(f"\nStart = {self.func_name} {args}")

    def change_function(self, func):
        self.func_name = func
        self.replace_function_name(func)

    def replace_function_name(self, func):
        fun_name = input('which one of these is ' + func + " ?:\t")
        if fun_name:
            self.content = self.content.replace(fun_name, func)
