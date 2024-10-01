## Polimorfismo 
- **O que é?**
    - Na programação, polimorfisomo significa o mesmo nome de função sendo usuado para tipos diferentes, ou seja, ele possui comportamentos diferentes. Como por exemplo a função **len**:
    ```Python
    len('Python')
    len([10, 5, 11])
    ```
    O mesmo recebe objetos diferentes, e para cada objeto ele se comporta de uma maneira. Dessa forma é possível concluir que _polimorfismo_ é o princípio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (mesma assinatura), porém com comportamentos diferentes.

- **Princípio da Substituição de Liskov**
    - Objetos de uma superclasses devem ser substituíveis por objetos de uma subclasse sem quebrar a aplicação.

- **Polimorfismo e Herança:**
    - Utilizado quando o método herdado da classe pai não se encaixa perfeitamente na classe filha.
    ```Python
    class Animal:
        def __init__(self, nome):
            self.nome = nome

        def falar(self):
            raise NotImplementedError("Subclasses devem implementar o método 'falar'.")

    class Cachorro(Animal):
        def falar(self):
            return f"{self.nome} diz: Au au!"

    class Gato(Animal):
        def falar(self):
            return f"{self.nome} diz: Miau!"

    # Função que demonstra o polimorfismo
    def fazer_animal_falar(animal):
        print(animal.falar())

    # Criando instâncias das subclasses
    cachorro = Cachorro("Rex")
    gato = Gato("Mingau")
    vaca = Vaca("Mimosa")

    # Usando o polimorfismo para fazer os animais "falarem"
    fazer_animal_falar(cachorro)
    fazer_animal_falar(gato)
    fazer_animal_falar(vaca)

    ```