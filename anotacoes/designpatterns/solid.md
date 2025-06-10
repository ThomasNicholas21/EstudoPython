# SOLID

**SOLID** é um acrônimo para cinco princípios de design de software que visam tornar sistemas mais compreensíveis, flexíveis e fáceis de manter. Esses princípios ajudam a criar softwares:

* **Robustos**: menos propensos a falhas
* **Flexíveis**: mais adaptáveis a mudanças
* **Reutilizáveis**: componentes aplicáveis em diversos contextos
* **Manuteníveis**: fáceis de entender, testar e modificar

---

## **S** – Single Responsibility Principle (SRP)

**"Uma classe deve ter apenas uma razão para mudar."**
Cada classe deve ter uma única responsabilidade bem definida. Ao separar responsabilidades, evita-se que mudanças em uma parte afetem outras.

**Exemplo ruim**: uma classe `Funcionario` que calcula salário, gera relatórios e envia e-mails.
**Melhoria**: criar classes específicas como `CalculadorDeSalario`, `GeradorDeRelatorio`, e `ServicoDeEmail`.

**Benefícios**:

* Alta coesão
* Baixo acoplamento
* Facilita testes e manutenção

---

## **O** – Open/Closed Principle (OCP)

**"Entidades de software devem estar abertas para extensão, mas fechadas para modificação."**
Você deve poder adicionar novos comportamentos sem alterar código existente, usando abstrações e polimorfismo.

**Exemplo ruim**: um `CalculadorDeDesconto` com muitos `if/else` para diferentes tipos de produto.
**Melhoria**: usar uma interface `RegraDeDesconto`, com implementações específicas para cada tipo.

**Benefícios**:

* Mais fácil de estender
* Evita quebrar funcionalidades existentes
* Promove reuso

---

## **L** – Liskov Substitution Principle (LSP)

**"Subtipos devem poder substituir seus tipos base sem alterar o funcionamento do sistema."**
Classes derivadas devem manter o comportamento esperado das classes base.

**Exemplo clássico**: `Quadrado` herdando de `Retangulo` e causando comportamento inesperado ao sobrescrever `setAltura` e `setLargura`.

**Melhoria**: usar composição ou interfaces que respeitem os contratos esperados.

**Benefícios**:

* Herança sem surpresas
* Polimorfismo confiável
* Código mais robusto

---

## **I** – Interface Segregation Principle (ISP)

**"Nenhum cliente deve ser forçado a depender de métodos que não usa."**
Prefira interfaces pequenas e específicas em vez de interfaces grandes e genéricas.

**Exemplo ruim**: interface `Trabalhador` com métodos `trabalhar`, `codificar`, `gerenciarProjetos`, etc.
Um gerente que não codifica seria forçado a implementar `codificar()`.

**Melhoria**: interfaces como `Codificavel`, `Gerenciavel` e `Trabalhavel`, separadas conforme responsabilidades.

**Benefícios**:

* Menor acoplamento
* Interfaces mais coesas
* Refatoração mais simples

---

## **D** – Dependency Inversion Principle (DIP)

**"Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações."**
Ao invés de depender diretamente de implementações, use interfaces.

**Exemplo ruim**: `ServicoDeRelatorios` que instancia diretamente `RepositorioSQL`.
**Melhoria**: criar interface `IRepositorio`, e injetar a dependência adequada.

**Benefícios**:

* Código mais flexível e testável
* Menor acoplamento
* Facilita troca de implementações

---