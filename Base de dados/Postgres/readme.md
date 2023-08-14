## Instruções de Execução

Siga estas etapas para executar o projeto:

1. **Clonar o Repositório**

   Clone o repositório e navegue até a pasta do projeto:
   ```shell
    git clone https://github.com/Gefte/educa-mvp.git
    
    cd nome_do_repositório

2. **Configurar o Banco de Dados PostgreSQL com Docker**
    
    ```shell
    cd Base de dados/Postgres
    
    docker-compose up -d
    
    docker-compose ps

3. **Configurar o Ambiente Virtual**
    
    ```shell
    python -m venv .venv
    
    source .venv/bin/activate

    pip install -r requirements.txt

4. **Executar o Script de Conexão ao PostgreSQL**

    ```shell
    python scripts-python/conexao-postgress.py


