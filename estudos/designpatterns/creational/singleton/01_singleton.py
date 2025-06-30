"""
Exemplo prático para entender o padrão de projeto Singleton.

Componentes principais:
- Singleton
- Client
"""


class AppSettings:
    _intance = None
    _initialized = False  # Solução para não sobrescrever a inicialização.

    def __new__(cls, *args, **kwargs):  # cria uma nova classe
        if not cls._intance:
            cls._intance = super().__new__(cls, *args, **kwargs)
        return cls._intance

    def __init__(self):
        if not self.__class__._initialized:
            self.host = 'admin'
            self.port = '8000'
            self.__class__._initialized = True


if __name__ == "__main__":
    app_settings_1 = AppSettings()
    app_settings_1.host = 'test'
    print(app_settings_1.host)

    app_settings_2 = AppSettings()
    print(app_settings_1.host)
