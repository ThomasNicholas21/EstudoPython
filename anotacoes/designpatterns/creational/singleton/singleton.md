# Singleton
O Singleton visa garantir que uma classe tenha somente uma instância e fornece um ponto global de acesso para a mesma, comumente utilizada para configuração do sistema, no qual geralmente é única no sistema. Resolve problemas como:
- `Inconsistência de configuração`
- `Uso ineficiente de recursos compartilhados (ex: conexões DB)`
- `Dificuldade no controle centralizado (ex: logs, settings globais)`

**Vantagens do Singleton**
- `Garantia de Única Instância`
- `Acesso Global Controlado`
- `Economia de Recursos`
- `Gerenciamento de Recursos Compartilhados`

**Desvantagens do Singleton**
- `Dificuldade de Teste Unitário`
- `Oculta Dependências`
- `Acoplamento Forte`
- `Pode Levar a "Anti-Padrões"`

**Quando Usar o Singleton**
- Quando deve haver exatamente uma instância de uma classe, e ela deve ser acessível a partir de um ponto de acesso bem conhecido.
- Quando é necessário garantir acesso global consistente a um único recurso.

**Alternativas para contornar as desvantagens do Singleton**
- Injeção de Dependência (DI)
- Factory
- Double-Checked Locking (DCL): usado para otimizar a criação do Singleton em ambientes multi-threaded. Mais comum em Java/C++. Em Python, usa-se threading.Lock() com cuidado para garantir segurança de thread.

## Componentes Principais:
- Singleton (classe):
O estereótipo <<Singleton>> é uma convenção para indicar que esta classe segue o padrão Singleton.
- {static} instance: Singleton: Um atributo estático ({static}) e privado (-) que irá armazenar a única instância da classe Singleton.
- Singleton(): Em linguagens como Java ou C++, o construtor é privado. Em Python, controlamos isso via __new__ e atributos de classe, pois não existe modificador de acesso nativo.
+ {static} getInstance(): Singleton: O método público (+) e estático ({static}) que é o ponto de acesso global à instância. É por meio dele que se obtém a única instância de Singleton.
+ someBusinessLogic(): void: Outros métodos de negócio que o Singleton implementa.

- Client (classe):
Client --> Singleton : <<uses>>: Indica que a classe Client interage com a classe Singleton (chamando Singleton.getInstance()).

## Exemplos
- Clique [👉 aqui](https://github.com/ThomasNicholas21/EstudoPython/tree/master/estudos/designpatterns/creational/singleton)