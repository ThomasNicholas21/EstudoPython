# Builder
O *Builder* permite que você produza diferente tipos de representãoções de um objeto usando o mesmo código de construção.

Ou seja, você separa a construção de um objeto complexo da sua representação final, possibilitando a criação do mesmo com variações diferentes.


**Vantagens do Builder**
- Constroi objetos passo a passo
- Reaproveita código
- SRP - SOLID

**Desvantagens do Builder**
- Aumento da complexidade do código

**Quando Usar o Builder**
Quando um objeto possui diversos parâmetros, podendo sobrecarregar o construtor. No caso do *Python*, não é muito utilizado pela linguagem suportar argumentos nomeados, construção de objetos e entre outros.

## Componentes Principais:
* **`Builder` (classe):**
  * O Builder é uma *interface* que possui o processo de construção de um produto, juntamente ao **reset()**, responsável por limpar essa classe a cada construção.
  * `+reset()`
  * `+buildsteps()`

* **`Builders Concretos ` (classe):**
  * Builders concretos, são responsáveis pela concretização da construção de um determinado produto.
  * `+reset()`
  * `+buildsteps()`
  * `+getresult()` -> Retorna resultado

* **`Produtos  ` (classe):**
  * Resultado da constru;cão de um produto

* **`Diretor ` (classe):**
  * São configurações de construções, definindo etapas pensando na reutilização do método

* **`Cliente ` (classe):**

  * `Cliente  --> Diretor : <<usa>>`
  * `Cliente  --> Builders Concretos : <<usa>>`

## Exemplos
- Clique [👉 aqui](https://github.com/ThomasNicholas21/EstudoPython/blob/master/estudos/designpatterns/creational/builder/01_builder.py)
