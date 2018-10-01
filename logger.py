class Logger:

    # TODO refactor
    @staticmethod
    def log(success, student, message=""):
        msg = "failed"
        if success:
            msg = "success"
        with open("results.txt", "a") as resultsfile:
            resultsfile.write(f'{student}\t\t{msg}\t\t{message}\n'.expandtabs(10))