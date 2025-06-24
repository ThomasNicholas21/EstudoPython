# Abstract Factory
Abstract Factry é um padrão de criação que fornece uma interface para criar famílias de objetos realcionados ou dependente, sem especificar suas classes concretas. Geralmente vai contar com um ou mais Factory Methods para criar seus objetos. O Abstract Factory utiliza composição para criar suas interfaces, diferente de Factory Method, que utiliza herança.

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
- `AbstractProduct (Produto Abstrato):`
    - Declara uma interface para um tipo de objeto produto. Existem vários AbstractProducts, um para cada tipo de produto na família.
    - `Ex:` Botao, CaixaDeTexto, Menu.

- `ConcreteProduct (Produto Concreto):`
    - Implementa uma interface AbstractProduct. São as implementações específicas de um produto para uma determinada família.
    - `Ex:` BotaoClaro, BotaoEscuro (para Botao); CaixaDeTextoClaro, CaixaDeTextoEscuro (para CaixaDeTexto).

- `AbstractFactory (Fábrica Abstrata):`
    - Declara uma interface para operações que criam cada tipo de AbstractProduct na família. Cada método retorna um tipo AbstractProduct.
    - `Ex:` GUIFactory (com métodos como criarBotao(), criarCaixaDeTexto(), criarMenu()).

- `ConcreteFactory (Fábrica Concreta):`
    - Implementa a interface AbstractFactory. Cada fábrica concreta é responsável por criar os ConcreteProducts de uma família específica.
    - `Ex:` TemaClaroFactory (que criaria BotaoClaro, CaixaDeTextoClaro, etc.); TemaEscuroFactory (que criaria BotaoEscuro, CaixaDeTextoEscuro, etc.).

- `Client (Cliente):`
    - Interage apenas com as interfaces AbstractFactory e AbstractProducts. Ele usa a fábrica para criar os produtos e os produtos para operar neles, sem conhecer suas classes concretas.

## Exemplos
- Clique [👉 aqui](https://github.com/ThomasNicholas21/EstudoPython/blob/master/estudos/designpatterns/creational/factories/factory_method.py)