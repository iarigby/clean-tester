def log(success, student, message=""):
    msg = "failed"
    if success:
        msg = "success"
    write_message(f'{student}\t\t{msg}\t\t{message}')


def write_message(message, ending="\n"):
    print(message)
    with open("results.txt", "a") as resultsfile:
        resultsfile.write(message.expandtabs(10) + ending)


from enum import Enum


class Confirmations(Enum):
    UNZIP_MAIN_FILE = "unzip main file"
    ERASE_SOURCE_DIR = "erase source directory"
    CONTINUE = "continue"
    ADDITIONAL_COMMENTS = "add additional comments"
    RECHECK_SUBMISSION = "done evaluating? press r to reload file and rerun tests"

    def get_question(self):
        return f"should I {self.value}? y or press enter to skip"

    @staticmethod
    def get_members():
        return list(Confirmations.__members__)


class InputHandler:

    def __init__(self, default_value=True):
        self.confirmations = {member: default_value for member in Confirmations.get_members()}

    def disable(self, confirmation):
        self.confirmations[confirmation] = False

    def enable(self, confirmation):
        self.confirmations[confirmation] = True

    def confirm(self, confirmation: Confirmations):
        if self.confirmations[confirmation.name]:
            return input(confirmation.get_question())
        return False
