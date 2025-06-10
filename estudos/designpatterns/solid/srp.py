"""
🔹 S - Single Responsibility Principle (SRP)
Exercício: Refatorar uma classe Usuario que atualmente faz tudo: cadastro,
envio de email e validação. A ideia é separar essas responsabilidades em
classes específicas.
"""


class User:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def validar_dados(self):
        if "@" not in self.email:
            raise ValueError("Email inválido")
        if len(self.senha) < 6:
            raise ValueError("Senha muito curta")
        print("Validação concluída.")

    def salvar_no_banco(self):
        print(f"Salvando usuário {self.nome} no banco de dados...")

    def enviar_email_boas_vindas(self):
        print(f"Enviando email de boas-vindas para {self.email}...")

    def cadastrar(self):
        self.validar_dados()
        self.salvar_no_banco()
        self.enviar_email_boas_vindas()
        print("Usuário cadastrado com sucesso!")
