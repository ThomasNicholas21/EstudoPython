# Abstract Factory
Abstract Factory é um padrão de criação que fornece uma interface para criar famílias de objetos relacionados ou dependentes, sem especificar suas classes concretas. Geralmente conta com um ou mais Factory Methods para criar seus objetos. Diferente do Factory Method, que utiliza herança, o Abstract Factory utiliza composição para criar suas interfaces.

**Vantagens do Abstract Factory**
- Desacoplamento entre a criação e o uso de objetos (aderência ao princípio OCP - Open/Closed Principle).
- Facilidade de manutenção e extensão, ao permitir adicionar novas famílias de produtos com pouca ou nenhuma modificação no código existente.
- Consistência entre objetos criados: todos pertencem à mesma família.
- Organização e modularidade: a lógica de criação fica centralizada em fábricas específicas.

**Desvantagens do Abstract Factory**
- Aumento da complexidade estrutural, especialmente em sistemas pequenos ou simples.
- Dificuldade de modificação se for necessário adicionar um novo tipo de produto em todas as fábricas existentes.
- Pode se tornar verboso e confuso em sistemas muito grandes, com muitas famílias de objetos (problema do paralelismo).

**Quando Usar o Abstract Factory**
- Quando o sistema deve ser independente de como seus objetos são criados, compostos e representados.
- Quando o sistema deve ser configurado com uma das várias famílias de objetos.
- Quando se deseja garantir que os objetos de uma mesma família sejam utilizados juntos.
- Quando você quer centralizar a criação dos objetos e facilitar testes, injeções e trocas de implementação.
- Quando a criação de objetos deve seguir uma lógica complexa que varia conforme o contexto (como no exemplo de Logística).


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