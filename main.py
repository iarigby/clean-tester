from config import Config
from submissionChecker import SubmissionChecker
from dataReprs import SubmissionData
from helpers import *


def main():
    open('results.txt', 'w').close()
    conf = Config("a.out", "test", "source", ".")
    functions = get_test_data("resources/tests2.json").hw2
    submission_data = SubmissionData("hw2", "hw2", functions)
    session = SubmissionChecker(submission_data, conf)
    session.start_session()

main()
