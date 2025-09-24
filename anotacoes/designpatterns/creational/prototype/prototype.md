# Prototype
O Prototype é um padrão de projeto criacional que permite a clonagem de objetos, mesmo complexos, sem acoplamento à suas classes específicas. Trazendo como solução, o próprio método ao objeto que está sendo clonado, permitindo a clonagem do sem aclopamento

Dessa forma, ele vai especificar os tipos de objetos a serem criados usando uma instância do protótipo e criar novos objetos pela cópia desse protótipo. Vale lembrar que esse padrão de projeto já está implementando na linguagem `python`

**Vantagens do Prototype**
- Você pode clonar objetos sem acoplá-los a suas classes concretas.
- Você pode se livrar de códigos de inicialização repetidos em troca de clonar protótipos pré-construídos.
- Você pode produzir objetos complexos mais convenientemente.
- Você tem uma alternativa para herança quando lidar com configurações pré determinadas para objetos complexos.

**Desvantagens do Prototype**
- Clonar objetos complexos que têm referências circulares pode ser bem complicado.

**Quando Usar o Prototype**
- Quando seu código não depender de classes concretas de objetos que precisa copiar
- Utilizar quando é necessário reduzir o número de subclasses

## Componentes Principais:
- Client
    - Produz a cópia do objeto que segue a interface do Prototype.
- Prototype
    - Interface que declara métodos de clonagem
- ConcretePrototype
    - implementa o método de clonagem. Além de copiar os dados do objeto original para o clone, esse método também pode lidar com alguns casos específicos do processo de clonagem relacionados a clonar objetos ligados, desfazendo dependências recursivas, etc.
- SubclassPrototype

## Exemplos
- Clique [👉 aqui](https://github.com/ThomasNicholas21/EstudoPython/blob/master/estudos/designpatterns/creational/prototype/01_prototype.py)