import os

from bcolors import *
from helpers import *

print("started")
test_directory = "test"
filename = "ex1"
exe_name = "a.out"

with open(f"{filename}.icl", "r") as read_file:
    contents = read_file.read()

if not os.path.exists(test_directory):
    os.makedirs(test_directory)

contents = contents.replace("\n Start", "//Start")
contents = contents.replace("\nStart", "//Start")


def create_test_file(clean_function, arguments):
    with open(f'{test_directory}/{filename}.icl', 'w+') as testfile:
        testfile.write(contents)
        testfile.write(f"\nStart = {clean_function} {arguments}")


def test_function(function_data):
    print(f"*** {OKBLUE}testing function {function_data.name} {ENDC}***")
    run_tests(function_data.name, function_data.tests.shown)
    run_tests(function_data.name, function_data.tests.hidden)


def run_tests(function_name, test_list):
    for test in test_list:
        run_test(function_name, test.input, test.output)


def run_test(f_name, f_input, f_output):
    create_test_file(f_name, f_input)
    make_call(f"clm -l -no-pie -nt -I {test_directory} {filename} -o {test_directory}/{exe_name}")
    exe_path = f"./{test_directory}/{exe_name}"
    # TODO can do this with err return of make_call
    if os.path.exists(exe_path):
        output = make_call(exe_path)
        print(f"\t\t returned {check_output(output, f_output)} for input {f_input}")
    else:
        print("there was an error during compilation")


def check_output(output, f_output):
    if output.strip() == str(f_output):
        return OKGREEN + "success" + ENDC
    else:
        return FAIL + "failed" + ENDC


def main():
    data = get_test_data("tests.json")
    for func in data.classwork1:
        test_function(func)


main()
