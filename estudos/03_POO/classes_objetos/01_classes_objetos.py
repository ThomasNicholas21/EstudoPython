class Calculadora: # Definindo classe
    def ad(self, numero1, numero2): # Definindo Metodos
        return numero1 + numero2
    
    def sub(self, numero1, numero2): # Definindo Metodos
        return numero1 - numero2 

#Instanciando objeto com características e metodos da classe
calc = Calculadora()
resultado1 = calc.ad(2, 2)
resultado2 = calc.sub(3, 1)
print(resultado1)
print(resultado2)
