"""
Exemplo prático para entender o padrão de projeto Singleton.

Componentes principais:
- Singleton
- Client
"""


def singleton(cls):
    instances = {}

    def get_class(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        self.host = 'admin'
        self.port = '8000'


if __name__ == "__main__":
    app_settings_1 = AppSettings()
    app_settings_1.host = 'test'
    print(app_settings_1.host)

    app_settings_2 = AppSettings()
    print(app_settings_1.host)
