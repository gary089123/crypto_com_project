import os
import yaml
import logging

class TestSetReader():

    def __init__(self, testset='/testset.yaml') -> None:
        self.path = os.getcwd() + testset
        self.yaml_data = self.read_yaml(self.path)

    def read_yaml(self, path):

        data = None

        with open(path, "r") as f:
            try:
                data = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                logging.error(exc)

        return data

    def get_run_tests(self):

        testset = self.yaml_data["configuration"]["testset"]
        tests = self.yaml_data["testsets"][testset]

        return tests

    def get_run_config(self, key):
        
        return self.yaml_data["configuration"][key]
    


    def get_testset_data(self):

        return self.yaml_data
            



