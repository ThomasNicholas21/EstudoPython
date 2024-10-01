# Interfaces
- Interfaces definem o que uma classe deve fazer e não como. Este conceito seria como definir um contrato aonde são declarados os metodos (O que deve ser feito) e suas rescpectivas assinaturas. Porém em python não existe palavras reservadas para o mesmo, se utilizando classes abstratas para criar contratos, pois os mesmos não podem ser instnaciados.

# Classes Abstratas
- Classes abastratas são aquelas que não podem ser instanciadas diretamente, servindo como modelo para ouitras classes (contratos). Sendo elas utilizadas para definir modelos que devem ser implementadas por subclasses, garantindo que sigam uma interface específica.
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