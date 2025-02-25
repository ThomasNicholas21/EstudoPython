# Interfaces
- Interfaces definem o que uma classe deve fazer e não como deve fazer. Este conceito seria como definir um contrato aonde são declarados os métodos (O que deve ser feito) e suas respectivas assinaturas. Porém em python não existe palavras reservadas para o mesmo, se utilizando classes abstratas para criar contratos, pois os mesmos não podem ser instanciados.

# Classes Abstratas
- Classes abstratas são aquelas que não podem ser instanciadas diretamente, servindo como modelo para outras classes (contratos). Sendo elas utilizadas para definir modelos que devem ser implementados por subclasses, garantindo que sigam uma interface específica.
- Python não vem nativamente com classes abstratas, por isso deve-se chamar o módulo abc (Abstract Base Class) para criar classes abstratas. Sendo elas marcadas por decoradores '@abstractmethod'.

- **Quando Usar?**
    - Definir um interface clara: quando se tem um conjunto de classes que devem compartilhar um conjunto comum de métodos.
    - Consistência: garantir que subclasses seguirão uma estrutura específica.
    - Bibliotecas e APIs: classes abstratas são úteis para criação de funcionalidades específicas de acordo com uma interface.

- **Vantagens**
    - Consistencia: garante uma estrutura
    - Flexibilidade: permite diferentes implantações
    - Segurança: força a implementação dos métodos obrigatórios

- **Desvantagens**
    - Complexidade
    - Restrição

- **Exemplo**
    ```python
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

### 👉 [Mais exemplos e atividades](https://github.com/ThomasNicholas21/EstudoPython/tree/master/estudos/03_POO/classes_variaveis_metodos)

