import teste

print(dir(teste)) # mostra todos os atributos de um objeto
# Saída - ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# DocStrings
print(teste.__doc__) # Acessa a documentação do código definida no arquivo teste.py

print(help(teste)) # Exibe informções detalhadas sobre um objeto, módulo, função, classe oui método, mostrando sua documentação e explicando seu uso