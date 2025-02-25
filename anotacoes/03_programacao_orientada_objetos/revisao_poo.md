# Pragramação Orientada a Objetos (POO)
Paradigma de programação é um estilo de programação de como solucionar problemas através do código. O paradigma de programação orientada a objetos faz a estruturação do código abstraindo problemas em objetos do mundo real, facilitando o entendimento do código e tornando-o mais flexível e modular.

## Classes e Objetos
- **```Classes```**
    - É o que define as características e comportamentos de um objeto, porém não é possível utilizar diretamente, ou seja, é algo abstrato.
- **```Objetos```**
    - O objeto instanciado por uma classe pode utilizar as características e comportamentos que foram definidos na classe.

Exemplo:
```python
class Calculadora:
    def somar(self, a, b):
        return a + b

calc = Calculadora()
resultado = calc.somar(3, 4)
print(resultado)  # 7
```

## Contrutores e Destrutores
- **```Método Contrutor```**
    - Inicializa de forma automática os atributos do objeto, chamado quando uma nova instância da classe é criada, sendo chamado de: ```__init__ ```
    Exemplo:
    ```python
    class MinhaClasse:
        def __init__(self, parametros):
            # Inicialização dos atributos
            self.atributo1 = valor1
            self.atributo2 = valor2
    ```
- **```Método Destrutor```**
    - Ele é chamado para realizar a destruição de um objeto, ou seja, para remover o objeto da memória. Ele é menos utilizado em Python, pois a linguagem possui um recurso de coletor de lixo, porém aquele que não é removido o método se torna útil, como por exemplo: conexões de rede ou recursos externos. Sendo representado por: ```__del__```.

    Exemplo:
    ```python
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
            print(f'{self.nome} foi criado.')

        def __del__(self):
            print(f'{self.nome} está sendo destruído.')git s

    # Criando uma instância da classe Pessoa
    pessoa1 = Pessoa("João", 30)

    # Deletando a instância explicitamente
    del pessoa1
    ```

## Herança
- **O que é?**
    - Na programação orientada a objeto, herança é a capacidade de uma classe filha herdar as caractéristicas e comportamento da classe pai.
- **Vatangens:**
    - Faz a reutilização do código, para que não seja necessário repetir. Além disso, permite adicionar mais recursos a uma classe sem modificá-la.
    - É transitiva, caso uma classe B herde da classe A, todas as sublcasses de B heradarão de forma automatica da classe A, ou seja, caso a classe B tenha como filha a classe C, essa classe será neta da classe A herdando suas caractéristicas.
        - **Obs:** Sempre verificar a complexidade da herança das classe, pois caso a fámilia seja grande, uma pequena alteração irá refletir em toda a familia.
## **Herança Simples**
- Quando uma classe filha herda apenas uma classe pai, essa é chamada de herança simples 
```python
class A:
    pass
class B(A): # Filha da classe A
    pass
```
## **Herança Múltipla**
- Quando uma classe filha herda de várias classes pai, ela é chamada de herança múltipla.
```python
class A:
    pass
class B: 
    pass
class C(A, B): # Herda caractéristicas da classe A e B
    pass
```

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
    - **property():** possibilita criar atributos que são gerenciados em suas classes, podendo usar atributos gerenciados e também conhecidos como propriedade. Quando Precisar modificar sua implantacão interna sem alterar a API pública da classe.
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


## Polimorfismo 
- **O que é?**
    - Na programação, polimorfisomo significa o mesmo nome de função sendo usuado para tipos diferentes, ou seja, ele possui comportamentos diferentes. Como por exemplo a função **len**:
    ```Python
    len('Python')
    len([10, 5, 11])
    ```
    O mesmo recebe objetos diferentes, e para cada objeto ele se comporta de uma maneira.
- **Polimorfismo e Herança:**
    - Utilizado quando o método herdado da classe pai não se encaixa perfeitamente na classe filha.
    ```Python
    class Animal:
        def __init__(self, nome):
            self.nome = nome

        def falar(self):
            raise NotImplementedError("Subclasses devem implementar o método 'falar'.")

    class Cachorro(Animal):
        def falar(self):
            return f"{self.nome} diz: Au au!"

    class Gato(Animal):
        def falar(self):
            return f"{self.nome} diz: Miau!"

    # Função que demonstra o polimorfismo
    def fazer_animal_falar(animal):
        print(animal.falar())

    # Criando instâncias das subclasses
    cachorro = Cachorro("Rex")
    gato = Gato("Mingau")
    vaca = Vaca("Mimosa")

    # Usando o polimorfismo para fazer os animais "falarem"
    fazer_animal_falar(cachorro)
    fazer_animal_falar(gato)
    fazer_animal_falar(vaca)

    ```

# Váriaveis de Instância e de Classes
- **Varáveis de Instância:**
    - Esses são diferentes para cada objeto, ou seja, possuem valores diferentes para cada cópia de objeto. **Exemplo:**
    ```Python
    class Pessoa:
        def __init__(self, nome, idade):
            self.nome = nome             # Variáveis de instância
            self. idade = idade
    
    pessoa1 = Pessoa('Fulano', 21)       # Muda para cada objeto instanciado
    pessoa2 = Pessoa('Ciclano', 22)
    ```
- **Variáveis de Classe:**
    - Atributos de classe são compartilhados em todos os objetos, ou seja, este atributo será compartilhado por todo objeto instanciado da classe. **Exemplo:**
    ```Python
    class Pessoa:
        sobrenome = 'Lano' # Atributo compartilhado entre os objetos instanciados dessa classe.

        def __init__(self, nome, idade):
            self.nome = nome
            self.idade = idade
        
    ```

# Métodos de classe e Métodos Estáticos
- ## Métodos de Classe
    - **O que são?**
        - Este método está apontado para classe e não para o objeto, ou seja, eles têm acesso ao estado da classe. Podendo ser chamado tanto de classe quanto de instâncias da classe, tradicionalmente conhecidos como **cls**.
    - **Quando Usar?**
        - Usado para motificar o estado da classe como um todo, e não a instância especifica, assim sendo, são úteis quando o comportamento do método deve ser compartilhado as instâncias de classe.
    - **Como usar?**
        - Para definir se utiliza '@classmethod', e a convenção utilizada para definir o primeiro parametro é 'cls'.
    - **Exemplo**
        ```Python
        class conta_bancaria:
            taxa_de_juros = 0,02  # Váriavel de classe

            def __init__(self, titular, saldo):
                self.titular = titular
                self.saldo = saldo

            @classmethod
            def alterar_taxa_juros(cls, nova_taxa): # CLS referencia a classe
                cls.taxa_de_juros = nova_taxa

            def calcula_taxa_juros(self):
                return self.saldo * self.taxa_de_juros

        conta_bancaria.alterar_taxa_juros(0.08) # Utilizando método de classe
        ``` 
- ## Método estático
    - **O que são?**
        - Este método não estão vinculados nem à instância e nem á classe, sendo eles como funções normais, porém estão presentes na classe por fazer sentido. Os mesmos não operam sobre a instância 'self' e 'cls'.
    - **Quando Usar?**
        - É utilizado quando a função faz parte da lógica da classe, mas sem precisar modificar o estado da classe ou da instância, sendo úteis como funções auxiliares que estão logicamente relacionados a classe.
    - **Como usar?**
        - Para definir utiliza-se o decorador '@staticmethod', sem precisar utilizar nenhum parâmetro obrigatório.
    - **Exemplo**
        ```Python
        class Calc:
            @staticmethod
            def somar(a, b)
                return a + b

        resultado_soma = Calc.somar # Utilizando método de Estático
        ``` 

# Interfaces
- Interfaces definem o que uma classe deve fazer e não como. Este conceito seria como definir um contrato aonde são declarados os metodos (O que deve ser feito) e suas rescpectivas assinaturas. Porém em python não existe palavras reservadas para o mesmo, se utilizando classes abstratas para criar contratos, pois os mesmos não podem ser instnaciados.

# Classes Abstratas
- Classes abastratas são aquelas que não podem ser instanciadas diretamente, servindo como modelo para ouitras classes. Sendo elas utilizadas para definir modelos que devem ser implementadas por subclasses, garantindo que sigam uma interface específica.
- Python não vem nativamente com classes abstratas, por isso deve-se chamar o módulo ABC (Abstract Base Class) no módulo 'abc' para criar classes abstratas. Sendo elas marcadas por decoradores '@abstractmethod'.

- **Quando Usar?**
    - Definir um interface clara: quando se tem um conjunto de classes que devem compartilhar um conjunto comum de métodos.
    - Consistência: garantir que subclasses seguiram uma estrutura especifica.
    - Bibiliotecas e APIs: calssers bastratas são utéis para criação, para criar funcionalidade específicas de acordo com uma interface.

- **Vantagens**
    - Consistencia: garante uma estrutura
    - Flexibilidade: permite diferentes implantações
    - Segurança: força a implemntação dos métodos obrigatórios

- **Desvantagens**
    - Complexidade
    - Restrição

- **Exemplo**
```Python
from abc import ABC, abstractmethod

class pagamento(ABC)

    @abstractmethod
    def processamento_de_pagamento(self, valor):
        pass

class CartaoDCredito(Pagamento):
    def processamento_de_pagamento(self, valor):
        print(f'Processamento de {valor} efetuado no crédito.')

class CartaoDDebito(Pagamento):
    def processamento_de_pagamento(self, valor):
        print(f'Processamento de {valor} efetuado no débito.')

pagamento_cartaocredito = CartaoDCretido()
pagamento_cartao.processar_pagamento(100)
pagamento_cartaodebito = CartaoDDebito()
pagamento_cartao.processar_pagamento(150)
```

### 👉 [Mais exemplos e atividades](https://github.com/ThomasNicholas21/EstudoPython/tree/master/estudos/03_POO)