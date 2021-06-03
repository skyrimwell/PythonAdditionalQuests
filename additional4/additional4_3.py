class Num:
    def __init__(self, number):
        self.number = number

    def stack(self):
        print('PUSH ' + str(self.number))

    def __repr__(self):
        return str(self.number)


class Operation:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


class Add(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.number = int(self.num1.number + self.num2.number)

    def count(self):
        return self.number

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print('ADD')

    def __repr__(self):
        return '({} + {})'.format(self.num1, self.num2)


class Mul(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.number = int(self.num1.number * self.num2.number)

    def count(self):
        return self.number

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print('MUL')

    def __repr__(self):
        return '({} * {})'.format(self.num1, self.num2)


# Реализовать класс-посетитель PrintVisitor для печати выражения.
# Обойтись без операторов ветвления.
class PrintVisitor:
    def visit(self, expression):
        return expression


# Реализовать класс-посетитель CalcVisitor для вычисления выражения.
# Обойтись без операторов ветвления.
class CalcVisitor:
    def visit(self, expression):
        return expression.count()


# Реализовать класс-посетитель StackVisitor для порождения кода стековой машины по выражению.
# Обойтись без операторов ветвления.
class StackVisitor:
    def visit(self, expression):
        expression.stack()


# Добавьте классы Sub и Mul.
# В существующий код можно только добавлять новые строки, не изменяя старой части.
class Sub(Operation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)
        self.number = int(self.num1.number - self.num2.number)

    def count(self):
        return self.number

    def stack(self):
        self.num1.stack()
        self.num2.stack()
        print('SUB')

    def repr(self):
        return '({} - {})'.format(self.num1, self.num2)