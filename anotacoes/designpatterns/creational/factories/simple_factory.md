# Simple Factory
O Simple Factory, que seria uma fábrica simples ou fábrica estática, não é considerado um padrão de Projeto, porém é muito importante para entender os padrões de criação mais complexos como Factory Method e Abastract Factory. Dessa forma, essa padrão emcapsula a lógica de criação de objetos de difertentes tipo em uma única classe.

Assim sendo, quando se tem um código que prcisa criar diferentes tipos de objetos, e a lógica está toda espelhada pelo sistema, crie uma fábrica que possui um método para criar e retornar instâncias de diferentes classes, baseadas em algum parâmetro de entrada.

## Componentes Principais:
- `Produto (Product)`: Geralmente uma interface ou classe abstrata que define a interface comum para os objetos que a fábrica vai criar.
- `Produtos Concretos (Concrete Products)`: As implementações reais dos objetos que serão criados. Eles implementam/estendem a interface/classe abstrata do Produto.
- `Fábrica Simples (Simple Factory)`: Uma classe com um método (geralmente estático, mas não necessariamente) que recebe um parâmetro e, com base nele, cria e retorna uma instância de um Produto Concreto apropriado.

## Exemplos
- Clique [👉 aqui](https://github.com/ThomasNicholas21/EstudoPython/blob/master/estudos/designpatterns/creational/factories/simple_factorie.py)