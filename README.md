# Doable - Task Management Backend

## Introdução

Doable é uma API REST para gerenciamento de tarefas que permite aos usuários criar, organizar e acompanhar suas tarefas diárias. A aplicação suporta categorização de tarefas, definição de prazos, e diferentes status de tarefas (pendente, em andamento, concluída, atrasada).

## Tecnologias Utilizadas

- **Django**: Framework web para desenvolvimento rápido e limpo
- **Django REST Framework**: Toolkit para construção de APIs Web
- **PostgreSQL/SQLite**: Bancos de dados suportados
- **SimpleJWT**: Autenticação via JSON Web Tokens
- **DRF Spectacular**: Documentação automática da API (OpenAPI/Swagger)
- **PDM**: Gerenciador de dependências e pacotes Python

## Requisitos do Sistema

- Python 3.10 ou superior
- PDM (Python Dependency Manager)
- Banco de dados (PostgreSQL recomendado para produção, SQLite para desenvolvimento)

## Instalação

### Clonando o Repositório

```bash
git clone git@github.com:G2M-Corp/doable-backend.git

cd doable-backend
```

### Configurando o Ambiente

1. Crie um arquivo `.env` baseado no exemplo fornecido:

```bash
cp .env.exemplo .env
```

2. Edite o arquivo `.env` com suas configurações:

```
MODE=DEVELOPMENT  # DEVELOPMENT, PRODUCTION, MIGRATE
DEBUG=True
SECRET_KEY=django_insecure_gere_uma_chave_secreta
# DATABASE_URL=postgres://user:password@localhost:5432/doable (opcional, para PostgreSQL)
MY_IP=127.0.0.1
```

### Instalando Dependências

Usando PDM (recomendado):

```bash
pdm install
```

Ou pip:

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

### SQLite (Desenvolvimento)

Por padrão, o projeto usa SQLite em ambiente de desenvolvimento. Não é necessária configuração adicional.

### PostgreSQL (Produção)

1. Crie um banco de dados PostgreSQL
2. Adicione a URL de conexão no arquivo `.env`:

```
DATABASE_URL=postgres://user:password@localhost:5432/doable
```

### Migrações

Execute as migrações para criar as tabelas do banco de dados:

```bash
pdm run migrate
# ou
python manage.py migrate
```

### Criar Superusuário (Opcional)

```bash
pdm run createsuperuser
# ou
python manage.py createsuperuser
```

## Executando o Servidor de Desenvolvimento

```bash
pdm run dev
# ou
python manage.py runserver 0.0.0.0:19003
```

O servidor estará disponível em:

- Web: http://localhost:19003
- API: http://localhost:19003/api/
- Admin: http://localhost:19003/admin/
- Documentação: http://localhost:19003/api/swagger/

## Endpoints da API

A API fornece os seguintes endpoints principais:

- `/api/usuarios/`: Gerenciamento de usuários
- `/api/tarefas/`: Gerenciamento de tarefas
- `/api/categorias/`: Gerenciamento de categorias
- `/token/`: Obtenção de tokens JWT
- `/token/refresh/`: Atualização de tokens JWT

## Documentação

A documentação completa da API está disponível em:

- Swagger UI: `/api/swagger/`
- ReDoc: `/api/redoc/`
- Schema: `/api/schema/`

## Scripts Úteis

O projeto inclui alguns scripts úteis:

```bash
# Atualizar o IP no arquivo .env para desenvolvimento
pdm run pre_dev

# Executar testes
pdm run test

# Abrir shell do Django
pdm run shell

# Abrir shell plus (com imports automáticos)
pdm run shellp

# Criar dumps de dados
pdm run dumpdata

# Carregar dados de um dump
pdm run loaddata
```
