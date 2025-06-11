"""
🔹 S - Single Responsibility Principle (SRP)
Exercício: Refatorar uma classe Usuario que atualmente faz tudo: cadastro,
envio de email e validação. A ideia é separar essas responsabilidades em
classes específicas.
"""
LOG_LIST = []


class LogMixin:
    def log_error(self, *, error_text: str, type_error: Exception):
        error_dict = {
            "description": error_text,
            "type": type_error
        }
        LOG_LIST.append(error_dict)


class User:
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password


class ValidateData(LogMixin):
    def validate_email(self, user: User) -> bool:
        if '@' not in user.email:
            self.log_error(
                error_text="E-mail inválido",
                type_error=ValueError
            )
            return False
        return True

    def validate_password(self, user: User) -> bool:
        if len(user.password) < 6:
            self.log_error(
                error_text="Senha deve ser maior que 6 caracteres",
                type_error=ValueError
            )
            return False
        return True

    def validate(self, user: User) -> bool:
        return self.validate_email(user) and self.validate_password(user)


class CommitDb:
    def __init__(
        self,
        database_name: str = "Teste",
        database_password: str = "Teste",
        database_port: str = "Teste"
    ):
        self.database_name = database_name
        self.database_password = database_password
        self.database_port = database_port

    def commit(self, user: User):
        print(f"Acessando database {self.database_name}...")
        print(f"Salvando {user.name} no banco de dados...")


class Email:
    def send_welcome_email(self, user: User):
        print(f"Enviando e-mail de boas-vindas para {user.email}...")


class SignUp:
    def __init__(
            self,
            validator: ValidateData,
            email_sender: Email,
            db: CommitDb
            ):
        self.validator = validator
        self.email_sender = email_sender
        self.db = db

    def execute(self, user: User):
        print("Iniciando cadastro de usuário...")
        if not self.validator.validate(user):
            print("Erro ao validar dados. Cadastro abortado.")
            return

        self.db.commit(user)
        self.email_sender.send_welcome_email(user)
        print("Usuário cadastrado com sucesso!")


if __name__ == "__main__":
    user1 = User(name="Ana", email="ana@email.com", password="123456")

    validator1 = ValidateData()
    email_sender1 = Email()
    database1 = CommitDb()

    signup = SignUp(validator1, email_sender1, database1)
    signup.execute(user1)

    print()
    user2 = User(name="Ana", email="anaemail.com", password="123456")

    validator2 = ValidateData()
    email_sender2 = Email()
    database2 = CommitDb()

    signup = SignUp(validator2, email_sender2, database2)
    signup.execute(user2)

    print("\nLOG_LIST:", LOG_LIST)
