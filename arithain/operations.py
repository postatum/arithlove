class Operation:
    default = ()
    sign = ''

    def __init__(self, x, y):
        self.x, self.y = self.prepareArgs(x, y)

    def prepareArgs(self, x, y):
        return x, y

    def isValid(self, inp):
        self.result = self.run(self.x, self.y)
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

    def prepareArgs(self, x, y):
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

    def prepareArgs(self, x, y):
        if y > x:
            x, y = y, x
        # TODO: numA/numB should be a whole number
        return x, y

    def run(self, x, y):
        return x / y


OPERATIONS = {
    Sum.sign: Sum,
    Difference.sign: Difference,
    Multiplication.sign: Multiplication,
    Division.sign: Division
}
