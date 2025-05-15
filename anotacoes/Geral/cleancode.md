## Clean Code Python
- ### Importância de Clean Code
Manter o código limpo e legível é essencial para facilitar a manutenção, aumentar a produtividade e reduzir erros. Aqui estão algumas dicas importantes para escrever clean code em Python:

- ### Dicas de Clean Code
    - **Use Nomes Descritivos**: Variáveis, funções e classes devem ter nomes claros e descritivos.
        ```python
        # Bom
        def calcular_media(lista_de_numeros):
            # ...
        
        # Ruim
        def calc(lst):
            # ...
        ```

    - **Evite Comentários Desnecessários**: Comente apenas o necessário. O código deve ser autoexplicativo sempre que possível.
        ```python
        # Bom
        def verificar_se_eh_par(numero):
            return numero % 2 == 0
        
        # Ruim
        def verificar_se_eh_par(numero):
            # Verifica se o número é par
            return numero % 2 == 0
        ```

    - **Mantenha Funções e Métodos Curtos**: Funções e métodos devem fazer apenas uma coisa e fazê-la bem. Idealmente, não devem ter mais de 20 linhas.
        ```python
        # Bom
        def obter_dados_usuario():
            # ...
        
        def validar_dados_usuario():
            # ...
        
        # Ruim
        def obter_e_validar_dados_usuario():
            # ...
        ```

    - **Use Espaços em Branco para Melhorar a Legibilidade**: Utilize linhas em branco para separar blocos de código e melhorar a leitura.
        ```python
        # Bom
        def funcao_exemplo():
            valor = calcular_valor()
            
            if valor > 0:
                processar_valor(valor)
            
            return valor
        
        # Ruim
        def funcao_exemplo():
            valor = calcular_valor()
            if valor > 0:
                processar_valor(valor)
            return valor
        ```

    - **Consistência na Indentação**: Use 4 espaços por nível de indentação. Não misture espaços e tabulações.
        ```python
        # Bom
        for i in range(10):
            print(i)
            
        # Ruim
        for i in range(10):
        print(i)
        ```

    - **Evite Códigos Duplicados**: Se você se pegar copiando e colando código, considere refatorar para uma função ou método.
        ```python
        # Bom
        def calcular_area_retangulo(largura, altura):
            return largura * altura
        
        area1 = calcular_area_retangulo(10, 20)
        area2 = calcular_area_retangulo(15, 30)
        
        # Ruim
        area1 = 10 * 20
        area2 = 15 * 30
        ```

    - **Seja Explícito**: Prefira ser explícito ao invés de implícito. Código explícito é mais fácil de entender e menos propenso a erros.
        ```python
        # Bom
        def verificar_maioridade(idade):
            if idade >= 18:
                return True
            else:
                return False
        
        # Ruim
        def verificar_maioridade(idade):
            return idade >= 18
        ```

    - **Trate Exceções de Forma Apropriada**: Sempre lide com exceções, mas faça isso de forma que o código continue sendo legível e compreensível.
        ```python
        # Bom
        try:
            resultado = operacao_critica()
        except ErroEsperado as e:
            tratar_erro(e)
        
        # Ruim
        try:
            resultado = operacao_critica()
        except:
            pass
        ```

    - **Utilize List Comprehensions**: São uma maneira concisa e eficiente de criar listas.
        ```python
        # Bom
        quadrados = [x**2 for x in range(10)]
        
        # Ruim
        quadrados = []
        for x in range(10):
            quadrados.append(x**2)
        ```

    - **Documente seu Código**: Use docstrings para documentar funções, classes e módulos.
        ```python
        def funcao_exemplo(parametro):
            """
            Esta função faz algo muito importante.
            
            Args:
                parametro (tipo): Descrição do parâmetro.
            
            Returns:
                tipo: Descrição do retorno.
            """
            # ...
        ```