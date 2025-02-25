## Encapsulamento
- **O que é?**
    - É a ideia de agrupar dados, impondo métodos que manipulam os dados. Impondo restrições diretos a variáveis e métodos, evitando a modificação de dados, pódendo apenas ser modificada pelo método do dado. Garantindo a manipulação de dados de forma consistente e segura.
- **Como funciona?**
    - **Atributos públicos:** Acessíveis de qualquer lugar.
    - **Atributos protegidos:** Acessíveis dentro de classes e subclasses (Indicado por "_")
        - **Um "_":** Isso indica uma convenção, sinalizando que o metodo indicado é protegido e deve ser tratado como detalhe interno.
        ### **Exemplo:**
        ```python
        class conta_bancaria:
            def __init__(self, titular, saldo_inicial):
                self.titular = titular # Atributo público
                self._saldo = saldo_inicial # Atributo Protegido
        ```
    - **Atributos privados:** Acessíveis apenas dentro da classe (Indicado por "__")
        - **Dois "__":** Este indica que o atributo passará por um processo chamado **Name Mangling** tornando o mesmo privado, pois ele dificulta o acesso fora da classe. O mesmo deixa o atributo diferente do que ele foi declarado de forma intencional. Porém ainda é possível aceessa-lo. **Exemplo**
        ``` Python
        class conta_bancaria:
            def __init__(self, titular, saldo_inicial):
                self.titular = titular # Atributo público
                self.__saldo = saldo_inicial # Atributo Privado
            
            def obter_saldo(self):
                return self.__saldo 
        ```
    - **property():** possibilita criar atributos que são gerenciados em suas classes, podendo usar atributos gerenciados e também conhecidos como propriedade. Quando Precisar modificar sua implantacão interna sem alterar a API pública da classe. Uma propriedade do objeto, ela é um método que se comporta como um atributo, geramente utilizada para agir como um getter(obtem um atributo), evitar quebrar código do cliente , habilitar setter e executar ações ao obter um atributo.
        - **Getter:** método utilizado para obter um valor de um atributo privado ou protegido de uma classe, em Python chamamos a função decoradora property() para realizar a ação.
            ```Python
            class Pessoa:
                def __init__(self, nome):
                    self._nome = nome  # Atributo protegido

                @property
                def nome(self):        # Metodo utilizado para obter o valor
                    return self._nome

                nome1 = 'Fulano'
                print(nome1.nome)      # Possibilita verificar o nome
            ```
        - **Setter:** O mesmo é utilizado para atribuir um valor a um atributo protegido ou privado.
            ```python
            class Pessoa:
                def __init__(self, nome):
                    self._nome = nome

                @property
                def nome(self):
                    return self._nome

                @nome.setter            # Chamando o método setter para atribuir o nome
                def nome(self, novo_nome):
                    self._nome = novo_nome

            nome1 = 'Fulano'
            print(nome1.nome) 
            nome1.nome = 'Ciclano'  # Atribuindo nome
            ```

        - **Deleter:** método utilizado para deletar um atributo.
            ```python
            class Pessoa:
                def __init__(self, nome):
                    self._nome = nome

                @property
                def nome(self):
                    return self._nome

                @nome.setter
                def nome(self, novo_nome):
                    self._nome = novo_nome

                @nome.deleter
                def nome(self):
                    del self._nome


            nome1 = 'Fulano'
            print(nome1.nome) 
            nome1.nome = 'Ciclano' 
            del nome1.nome
            ```


### 👉 [Mais exemplos e atividades](https://github.com/ThomasNicholas21/EstudoPython/tree/master/estudos/03_POO/encapsulamento)
