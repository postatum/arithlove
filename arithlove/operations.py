class Operation:
    default = ()
    sign = ''

    def __init__(self, x, y):
        self.x, self.y = self.prepare_args(x, y)

    def prepare_args(self, x, y):
        return x, y

    def is_correct(self, inp):
        self.result = int(self.run(self.x, self.y))
        try:
            inp = int(inp)
        except ValueError:
            return False
        return self.result == inp

    def run(self, x, y):
        raise NotImplementedError


class Sum(Operation):
    default = (2, 2)
    sign = '+'

    def run(self, x, y):
        return x + y


class Difference(Operation):
    default = (2, 2)
    sign = '-'

    def prepare_args(self, x, y):
        if y > x:
            x, y = y, x
        return x, y

    def run(self, x, y):
        return x - y


class Multiplication(Operation):
    default = (2, 2)
    sign = '*'

    def run(self, x, y):
        return x * y


class Division(Operation):
    default = (2, 1)
    sign = '/'

    def prepare_args(self, x, y):
        if y > x:
            x, y = y, x
        if x % y != 0:
            x += (y - x % y)
        return x, y

    def run(self, x, y):
        return x / y


OPERATIONS = {
    Sum.sign: Sum,
    Difference.sign: Difference,
    Multiplication.sign: Multiplication,
    Division.sign: Division
}
