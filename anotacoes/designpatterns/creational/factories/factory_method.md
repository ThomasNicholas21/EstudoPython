# Factory Method
O Factory Method é um padrão de criação que permite definir uma interface para criar objetos, mas deixa as subclasses decidirem quais objetos criar, ou seja, a criação dos objetos são delegados as subclasses. O Factory Method permite adiar a instanciação para as subclasses, garantindo o baixo acolplamento entre classes.

**O Factory Method traz consigo vários benefícios, dentre eles:**
- Aderir o desacomplamento (OCP - Open/Closed Principle)
- Facilita a manutenção, implementação e teste de novos tipos de produtos.
- Deixa o código mais organizado.
- Consistência na criação de produtos.

**Pode trazer algumas desvantagens, como:**
- Aumento da complexidade, devido a isso, deve ser bem analisado antes de ser aplicado.
- Pode deixar confuso em sistema muitos grandes, acontecendo o paralelismo.

## Quando Usar o Factory Method
- Quando uma classe não pode prever a classe dos objetos que ela deve criar.
- Quando uma classe deseja que suas subclasses especifiquem os objetos a serem criados.
- Quando as classes delegam a responsabilidade de criação para uma das várias subclasses auxiliares, e você quer centralizar a criação dessa lógica (como no nosso exemplo de Logistica).

## Componentes Principais:
- `Product (Produto):`
    - Define a interface (geralmente uma interface ou classe abstrata) para os objetos que o Factory Method cria. É o tipo que o método fábrica retorna.
    - `Ex`: Documento (com operações como abrir(), salvar(), imprimir()).

- `ConcreteProduct (Produto Concreto):`
    - Implementa a interface Product. São os objetos reais que são criados.
    - `Ex`: DocumentoPDF, DocumentoWord, DocumentoPlanilha.

- `Creator (Criador):`
    - Declara o Factory Method, que retorna um objeto do tipo Product.
    - Pode definir uma implementação padrão do Factory Method que retorna um ConcreteProduct padrão.
    - Pode conter código que opera nos produtos criados pelo Factory Method, independente do tipo concreto do produto.
    - `Ex`: Aplicacao (com um método criarDocumento()). Este criarDocumento() seria o Factory Method.

- `ConcreteCreator (Criador Concreto):`
    - Sobrescreve o Factory Method para retornar uma instância de um ConcreteProduct específico.
    - `Ex`: AplicacaoPDF, AplicacaoWord, AplicacaoPlanilha, que sobrescreveriam criarDocumento() para retornar DocumentoPDF, DocumentoWord, DocumentoPlanilha, respectivamente.

## Exemplos
- Clique [👉 aqui](https://github.com/ThomasNicholas21/EstudoPython/blob/master/estudos/designpatterns/creational/factories/factory_method.py)