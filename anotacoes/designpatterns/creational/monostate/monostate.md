# Monostate
O **Monostate**, também conhecido como **Borg**, é uma variação do **Singleton** proposta por *Alex Martelli*. Sua principal intenção é garantir que o **estado do objeto seja igual para todas as instâncias**, ou seja, garantir que todas as instâncias de uma classe compartilhem o mesmo estado, mas permitindo que cada instância se comporte como um objeto normal.

Dessa forma, **em vez de garantir uma única instância**, como faz o Singleton, o Monostate **garante um único estado compartilhado**. Embora seja possível criar várias instâncias de uma classe Monostate, elas atuarão como se fossem a mesma, pois compartilham os mesmos dados subjacentes.

Apesar de **não fazer parte do catálogo de Design Patterns do GoF**, o Monostate é um padrão com uma proposta mais **"pythônica"**, sendo uma alternativa elegante ao Singleton em contextos onde o compartilhamento de estado é mais importante do que o controle da instância.


**Vantagens do Monostate**
- Permite múltiplas instâncias com estado único
- Mais fácil de testar do que `Singleton`
- Evita o uso de variáveis globais
- Reutilizável com herança

**Desvantagens do Monostate**
- O estado compartilhado pode ficar "escondido", dificultando a leitura do código
- Dificulta o rastreamento de dependências e fluxo de dados
- Não é thread-safe por padrão, mas pode ser tornado mais seguro com o uso de `threading.Lock`

**Quando Usar o Monostate**
- Você precisa de um estado global compartilhado, mas não quer restringir a criação de múltiplas instâncias.
- Precisa evitar os problemas clássicos do `Singleton` (teste unitário difícil, acoplamento forte).
- Quer ter uma API mais flexível (já que você pode instanciar normalmente).

## Componentes Principais:
* **`Monostate` (classe):**

  * O estereótipo `<<Monostate>>` indica que essa classe segue o padrão Monostate (ou Borg), onde todas as instâncias compartilham o mesmo estado.
  * **`- sharedState1: Tipo1` / `- sharedState2: Tipo2`:** Atributos compartilhados por todas as instâncias. São definidos como estáticos e representam os dados globais.
  * **`+ Monostate()`:** Construtor público, permite criar várias instâncias normalmente.
  * **`+ getSharedState1(): Tipo1` / `+ setSharedState1(valor: Tipo1): void`:** Métodos que acessam ou modificam os dados compartilhados. Funcionam como qualquer método de instância.
  * **`+ realizarAcao(): void`:** Métodos que executam ações usando o estado compartilhado. Também são métodos de instância.

* **`Cliente` (classe):**

  * `Cliente --> Monostate : <<usa>>`: Indica que a classe `Cliente` utiliza a classe `Monostate`, instanciando-a normalmente e acessando seu comportamento como qualquer outro objeto.

## Exemplos
- Clique [👉 aqui](https://github.com/ThomasNicholas21/EstudoPython/tree/master/estudos/designpatterns/creational/monostate)