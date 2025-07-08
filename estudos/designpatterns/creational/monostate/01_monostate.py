"""
Exemplo prático para entender o padrão de projeto Monostate.

Componentes principais:
- Monostate
- Client
"""


class StringClassMixin:
    def __str__(self):
        params = ', '.join(
            [
                f'{k}={v}'
                for k, v in self.__dict__.items()
            ]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Logger(StringClassMixin):
    _shared = {}

    def __init__(self):
        self.__dict__ = self._shared
        if not hasattr(self, 'logs'):
            self.logs = []

    def set_log(self, message, type):
        self.logs.append([message, type])

    def get_log(self):
        return self.logs


if __name__ == "__main__":
    log1 = Logger()
    log1.set_log('erro generico do logger 1', AttributeError)

    log2 = Logger()
    log2.set_log('erro generico do logger 2', ValueError)

    print(log1.get_log())
    print(log2.get_log())
