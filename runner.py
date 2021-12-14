import subprocess
import webbrowser
import os

from utils.testSetReader import TestSetReader
import logging


class Runner():

    def __init__(self) -> None:
        self.testset_config = TestSetReader()


    def run_tests(self):

        run_tests = self.testset_config.get_run_tests()
        report = self.testset_config.get_run_config("report")

        if len(run_tests) == 0:
            logging.warning("no test case to run !")
        run_tests_cmd = " or ".join(run_tests)
        
        config_cmd = f" --env ./testenv.yaml"
        report_cmd = f" --html={report} --self-contained-html"
        log_cmd = " -vvv --log-level=DEBUG"
        run_command = f"pytest -k \'{run_tests_cmd}\'" + config_cmd + report_cmd + log_cmd
        print(f"Run pytest with : {run_command}")
        logging.info(f"Run pytest with : {run_command}")

        p = subprocess.Popen(run_command,shell=True)
        p.wait()

        

    def open_report(self):

        report = self.testset_config.get_run_config("report")
        webbrowser.open(f'file://{os.getcwd()}/{report}')



if __name__ == "__main__":

    runner = Runner()
    runner.run_tests()
    runner.open_report()

