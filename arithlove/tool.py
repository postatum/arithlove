import argparse
import json
import os
import random
import sys

from . import operations as ops
from . import cheers


class TrainingTool:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parser = argparse.ArgumentParser(
            description='Start arithmetic training tool')
        parser.add_argument(
            'configFile', type=str, help='JSON config file path')
        self.args = parser.parse_args()

    def parseConfigFile(self):
        self.conf = json.load(open(self.args.configFile))
        for key, op in ops.OPERATIONS.items():
            if key not in self.conf:
                self.conf[key] = op.default
        self.conf = {key: val for key, val in self.conf.items()
                     if val is not None}
        self.confOps = list(self.conf.keys())

    def run(self):
        self.parseConfigFile()
        print('Starting training with config: {}'.format(self.conf))

        try:
            while True:
                self.runExercise()
        except KeyboardInterrupt:
            print('\n\nSee you soon!')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def pickNumber(self, digits):
        num = random.randrange(10**(digits-1) + 1, 10**digits)
        if num % 10 == 0:
            num += random.randrange(1, 9)
        return num

    def outputResult(self, op, inp):
        if op.isCorrect(inp):
            print('\033[92m{} \033[1;31m<3\033[0m'.format(
                cheers.randomCheer()))
        else:
            cheer = (
                "Oops, it's actually {}. "
                "Would love to see you try again!"
            ).format(op.result)
            print('\033[33m{}\033[0m'.format(cheer))

    def runExercise(self):
        opSign = random.choice(self.confOps)
        opKlass = ops.OPERATIONS[opSign]
        op = opKlass(
            self.pickNumber(self.conf[opSign][0]),
            self.pickNumber(self.conf[opSign][1])
        )
        exercise = '{}{}{} = '.format(op.x, opSign, op.y)
        inp = input(exercise)
        self.outputResult(op, inp)
