import argparse
import json
import os
import random
import sys

from arithlove import cheers
from arithlove import operations as ops


class TrainingTool:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        parser = argparse.ArgumentParser(
            description='Start arithmetic training tool')
        parser.add_argument(
            'configFile', type=str, help='JSON config file path')
        self.args = parser.parse_args()
        self.conf = {}
        self.conf_ops = []

    def parse_config_file(self):
        self.conf = json.load(open(self.args.configFile))
        for key, opr in ops.OPERATIONS.items():
            if key not in self.conf:
                self.conf[key] = opr.default
        self.conf = {key: val for key, val in self.conf.items()
                     if val is not None}
        self.conf_ops = list(self.conf.keys())

    def run(self):
        self.parse_config_file()
        print('Starting training with config: {}'.format(self.conf))

        try:
            while True:
                self.run_exercise()
        except KeyboardInterrupt:
            print('\n\nSee you soon!')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def run_exercise(self):
        opr_sign = random.choice(self.conf_ops)
        opr_klass = ops.OPERATIONS[opr_sign]
        opr = opr_klass(
            pick_number(self.conf[opr_sign][0]),
            pick_number(self.conf[opr_sign][1])
        )
        exercise = '{}{}{} = '.format(opr.x, opr_sign, opr.y)
        inp = input(exercise)
        output_results(opr, inp)


def output_results(opr, inp):
    if opr.is_correct(inp):
        print('\033[92m{} \033[1;31m<3\033[0m'.format(
            cheers.random_cheer()))
    else:
        cheer = (
            "Oops, it's actually {}. "
            "Would love to see you try again!"
        ).format(opr.result)
        print('\033[33m{}\033[0m'.format(cheer))


def pick_number(digits):
    num = random.randrange(10**(digits-1) + 1, 10**digits)
    if num % 10 == 0:
        num += random.randrange(1, 9)
    return num
