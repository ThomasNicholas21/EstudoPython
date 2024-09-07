# Requuirements em Python

## *pip*
- pip na linguagem Python serve para instalar bibliotecas não nativas no ambiente.
    ```
    > pip install 'nome_biblioteca'
    ```
- com pip também é possível verificar tudo que está instalado no ambiente.
    ```
    > pip freeze 
    ```
- nas versões atuais do pip é possível verificar quais versões das bibliotecas está disponível.
    ```
    > pip index versions "nome_biblioteca" # Verifica todas as versôes disponíveis
    > pip install "nome_biblioteca"=="versão_desejada"
    ```

## Requirements
- O mesmo serve para gerar todas as bibliotecas instaladas no ambiente para estar rodando o projeto.
    ```
    > pip freeza > requirements.txt # Gera um arquivo TXT no ambiente apontando bibliotecas e suas versões. 
    ```
    - Ao baixar, pode-se utilizar o requirements.txt para baixar as dependências em outro ambiente virtual.
        ```
        > pip install -r .\requirements.txt
        ```