
import contextlib


class Html:
    def __init__(self):
        self.data = ''

    @contextlib.contextmanager
    def body(self):
        elem = '<body>\n'
        self.data += elem

        try:
            yield {}
        except RuntimeError as err:
            print('error: ', err)
        finally:
            self.data += elem

    @contextlib.contextmanager
    def div(self):
        elem = '<div>\n'
        self.data += elem

        try:
            yield {}
        except RuntimeError as err:
            print('error: ', err)
        finally:
            self.data += elem

    def p(self, arg):
        self.data += '<p>' + arg + '</p>\n'



def test():
    html = Html()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')
    print(html.data)


if __name__ == '__main__':
    test()