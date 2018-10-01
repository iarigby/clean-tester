from config import Config
from submissionChecker import SubmissionChecker
from dataReprs import SubmissionData
from helpers import *


def main():
    conf = Config("a.out", "test", "source", ".")
    functions = get_test_data("resources/tests2.json").ex3
    submission_data = SubmissionData("cw1", "ex3", functions)
    session = SubmissionChecker(submission_data, conf)
    session.start_session()


main()
