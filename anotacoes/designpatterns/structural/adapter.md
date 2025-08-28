# Adpater
O Adapter é um padrão de projeto estrutural que permite objetos com interfaces incompatíveis colaborarem entre si. Sendo assim, ele cria uma adpatação de comunicação para outras classes.

Por exemplo, o sistema recebe dados de produtos somente em XML, porém o serviço utilizado para analisar esses produtos trabalha somente com json. Ai que entra o `Adapter`, ele é responsável por adaptar esses dados recebidos do produto em XML para Json, permitindo que o serviço utilizado para análise receba esses dados sem conflito.

O `Adapter` pode ser útil não só em conversão de dados, mas para adaptação dos dados recebidos de forma geral.

O padrão Adapter permite que você crie uma classe de meio termo que serve como um tradutor entre seu código e a classe antiga, uma classe de terceiros, ou qualquer outra classe com uma interface estranha.

**Vantagens do Adapter**
- SRP: Single Responsability Principle
- OCP: Open/Closed Principle

**Desvantagens do Adapter**
- A complexidade geral do código aumenta porque você precisa introduzir um conjunto de novas interfaces e classes. Algumas vezes é mais simples mudar a classe serviço para que ela se adeque com o resto do seu código.

**Quando Usar o Adapter**
- Quando uma classe externa, antiga ou de terceiro, fornece dados que devem ser traduzidos dentro do sistema para leitura e funcionamento adequado

## Componentes Principais:
- `Classe Adapter`
    - Possui métodos para tradução e adaptação dos dados

- `Service`
    - Classe que normalmente é de terceiro ou código legado

## Exemplos
- Clique [👉 aqui](https://github.com/ThomasNicholas21/EstudoPython/blob/master/estudos/designpatterns/structural/adapter)
