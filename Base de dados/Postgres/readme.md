#### Como executar.

* Clonar o repositório

* navegar até o repositório do postgress Base de dados/Postgres/dockerfile

* Digitar os comando na ordem abaixo, 1 por vez no terminal:
    1 - `docker-compose up -d`
    2 - `docker-compose ps`

* Crie um ambiente virtual e o ative:
    1 - Primeiro precisamos de um ambiente virtual para instalar as dependencias do projeto.
       * `python -m venv .venv`
    2 - E ative a virtualenv
        # Linux
        * `source .venv/bin/activate`
        # Windows Power Shell
        * `.\venv\Scripts\activate.ps1`

* Execute o comando: `pip install -r requirements.txt`

* rode o script conexao-postgress.py
    - `python3 scripts-python/conexao-postgress.py`

.
├── Base de dados
│   └── Postgres
│       ├── docker-compose.yml
│       ├── readme.md
│       └── readme.pdf
├── requirements.txt
└── scripts-python
    └── conexao-postgress.py
