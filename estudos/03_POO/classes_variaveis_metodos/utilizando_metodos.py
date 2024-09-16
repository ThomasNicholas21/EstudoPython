# Aplicando métodos de classe e estático
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def auth_connection(cls, user, password):
        connection = Connection()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log_message(msg):
        print('LOG:', msg)


user1 = Connection()
user1.user = 'Thomas'
user1.password = '123'
Connection.auth_connection('Thomass', '1234')
Connection.log_message('Mensagem do LOG')

