# Ambiente Virtual Python

- Um ambiente virtual carrega toda a instalação do Python para uma pasta no caminho escolhido. Ao ativar um ambiente virtual, a instalação específica do ambiente virtual será utilizada.
- Caso o ambiente virtual seja criado em uma versão específica do Python, essa será a versão utilizada no ambiente.

## venv - Módulo Utilizado para Criação de Ambiente Virtual

- Nomes comuns utilizados:
  - `venv`, `env`, `.venv`, `.env`

### Windows

```bash
pasta> python -m venv (nome_ambiente)       # Cria o ambiente virtual

pasta> nome_ambiente\Scripts\activate       # Ativa o ambiente virtual

pasta> deactivate                           # Desativa o ambiente virtual

```

ao executar este comando você estará criando 3 pastas
- Include: Contém arquivos de cabeçalho C/C++ necessários para compilar extensões que dependem de bibliotecas nativas.
- Lib: Toda instalação de pacotes de terceiros será armazenada nesta pasta.
- Scripts: Contém todos os executáveis utilizados no ambiente virtual, como a ativação, desativação e até mesmo a versão do Python que será utilizada.

## MacOS / Linux - sistema Unix

```bash
pasta> python -m venv (nome_ambiente)       # Cria o ambiente virtual

pasta> .venv/bin/activate                   # Ativa o ambiente virtual
pasta> source nome_ambiente/bin/activate    # Ativa o ambiente virtual

pasta> deactivate                           # Desativa o ambiente virtual

```

- bin: Contém todos os executáveis utilizados no ambiente virtual, como a ativação, desativação e até mesmo a versão do Python que será utilizada.
- include: Armazena arquivos da linguagem C/C++ necessários para compilar extensões que dependem de bibliotecas nativas.
- lib: Toda instalação de pacotes de terceiros será armazenada nesta pasta.