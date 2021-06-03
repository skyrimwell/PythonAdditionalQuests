from operator import add, mul, sub, truediv
import random

class Calculator(object):
    op = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }

    def to_suffix(self, s):
        res = ''
        st = []
        tokens = s.split()
        for token in tokens:
            if token in ['*', '/']:
                while st and st[-1] in ['*', '/']:
                    res += st.pop() + ' '
                st.append(token)
            elif token in ['+', '-']:
                while st and st[-1] != '(':
                    res += st.pop() + ' '
                st.append(token)
            elif token == '(':
                st.append(token)
            elif token == ')':
                while st[-1] != '(':
                    res += st.pop() + ' '
                st.pop()
            else:
                res += token + ' '
        while st:
            res += st.pop() + ' '
        return res

    def eva(self, s):
        st = []
        tokens = s.split()
        for token in tokens:
            if token not in self.op:
                st.append(float(token))
            else:
                n1 = st.pop()
                n2 = st.pop()
                st.append(self.op[token](n2, n1))
        return st.pop()

    def invoke(self, string):
        return self.eva(self.to_suffix(string))


def calc(s):
    calculator = Calculator()
    return calculator.invoke(s)

def test_calc():
    for _ in range(10000):
        start(gen())


def start(s):
    try:
        return calc.calc(s)
    except:
        pass


def gen():
    a = '+-*/'
    b = '()'
    return ' '.join(
        [' '.join(
            [''.join(
                [str(random.choice(range(9)))
                 for _ in range(random.choice(range(1, 5)))]),
                random.choice(a), random.choice(b)])
            for _ in range(random.choice(range(5)))])
