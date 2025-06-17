# Factory
Padrão de projeto de criação, ou seja, possui foco na forma como os objetos são criados, tornando o sistema mais independente da lógica de instanciação. 

Na programação orientada a objetos, `factory` (fábrica) refere-se a uma classe ou método que é responsável por criar objetos.

## Vantagens
- Permite criar um sistema com baixo acoplamento entre classes, porque ocultam as classes que criam objetos do código cliente.
- Facilita adição de novas classes ao código, por que o cliente não conhece e nem utiliza a implementação da classe (utiliza a factory)
- Podem facilitar o processo de `cache` ou criação de `singletons` porque a fábrica pode retornar um objeto já criado para o cliente, ao invés de criar novos objetos sempre que o cliente precisar.

## Desvantagens
- Podem introduzir muitas classes no código.