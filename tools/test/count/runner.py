from time import sleep
from tools.test.count.flat.flat_duration import FlatDurationTest


class RunnerTestCount:
    def __init__(self):
        self._list_test = [
            FlatDurationTest()
        ]

    def execute(self):
        for list_type_test in self._list_test:
            list_type_test.execute()
            sleep(1)