# Requirements em Python

## *pip*
- `pip` na linguagem Python serve para instalar bibliotecas não nativas no ambiente.
    ```
    > pip install 'nome_biblioteca'
    ```
- Com `pip` também é possível verificar tudo que está instalado no ambiente.
    ```
    > pip freeze 
    ```
- Nas versões atuais do `pip`, é possível verificar quais versões das bibliotecas estão disponíveis.
    ```
    > pip index versions "nome_biblioteca" # Verifica todas as versões disponíveis
    > pip install "nome_biblioteca"=="versão_desejada"
    ```

## Requirements
- O `pip freeze` serve para gerar um arquivo com todas as bibliotecas instaladas no ambiente, permitindo que o projeto seja executado em outro ambiente.
    ```
    > pip freeze > requirements.txt # Gera um arquivo TXT no ambiente apontando bibliotecas e suas versões.
    ```
    - Ao baixar o projeto, pode-se utilizar o `requirements.txt` para instalar as dependências em outro ambiente virtual.
        ```
        > pip install -r .\requirements.txt
        ```