import argparse
import json
import random

from . import operations as ops


class TrainingTool:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parser = argparse.ArgumentParser(
            description='Start arithmetic training tool')
        parser.add_argument(
            'configFile', type=str, help='JSON config file path')
        self.args = parser.parse_args()
        self.operation = None

    def parseConfigFile(self):
        self.conf = json.load(open(self.args.configFile))
        for key, op in ops.OPERATIONS.items():
            if key not in self.conf:
                self.conf[key] = op.default
        self.confOps = list(self.conf.keys())

    def run(self):
        self.parseConfigFile()
        print('Starting training with config: {}'.format(self.conf))

        while True:
            self.runExercise()

    def pickNumber(self, digits):
        return 1

    def runExercise(self):
        opSign = random.choice(self.confOps)
        opKlass = opts.OPERATIONS[opSign]
        self.operation = opKlass(
            self.pickNumber(self.conf[opSign][0]),
            self.pickNumber(self.conf[opSign][1])
        )
