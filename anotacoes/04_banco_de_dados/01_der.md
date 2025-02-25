# Diagramas entidade relacionamento (DER)
- Uma abstração da parte do sistema a ser desenvolvido. O diagrama possui entidades e seus relacionamentos.
- *Exemplo:*
![alt text](image.png)
- O DER é a representação gráfica do MER (Modelo Entidade-Relacionamento). O MER diz que a exepressão da realidade se baseia no relacionamento entre as entidades 

## Entidades
- São objetos do mundo real que podem ser represantados no DER como tabelas, que possuem os atributos. 
    - **Chave Primária (PK)**
        - Valor sempre será único.
        - Não pode ser nulo.
        - A Chave primária é única.
        - Não pode ser alterada.
    - **Chave estrangeira (FK)**
        - Referencia uma chave primária de uma tabela em outra tabela.

    - **Relacionamento de Entidades**
        - *Um para Um*: indica que um registro está ligado a outro registro de outra tabela, sendo essencial ver a obrigatoriedade do mesmo.
        - *Um para Muitos*: quando um registro de uma tabela está atrelado a um ou muitos registros de outra tabela
        - *Muito para Muitos*: esse tipo de relacionamento se refere quando muitos registros de uma tabela se relaciona com muitos de outras tabelas, porém eles não podem se repetir.

    - Entidades Fortes
    - Entidades Fracas
    - Entidades Associativas
