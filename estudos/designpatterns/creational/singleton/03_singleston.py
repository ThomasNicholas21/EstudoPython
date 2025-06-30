"""
Exemplo prático para entender o padrão de projeto Singleton.

Componentes principais:
- Singleton
- Client
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return super().__call__(*args, **kwargs)


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.host = 'admin'
        self.port = '8000'


if __name__ == "__main__":
    app_settings_1 = AppSettings()
    app_settings_1.host = 'test'
    print(app_settings_1.host)

    app_settings_2 = AppSettings()
    print(app_settings_1.host)
