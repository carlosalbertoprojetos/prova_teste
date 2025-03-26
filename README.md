# prova_teste
Esse desafio envolve um CRUD completo em Django com PostgreSQL e um frontend separado utilizando HTML5 + Bootstrap 5. O backend seguirá a arquitetura proposta, separando as responsabilidades em Controller, Service e Task.

# Guia de Instalação

## Pré-requisitos
- Python 3.8 ou superior
- PostgreSQL 12 ou superior
- Git
- Ambiente de desenvolvimento (VSCode recomendado)

## Instalação em Windows

### 1. Preparação do Ambiente
1. Baixe e instale o Python (https://www.python.org/downloads/)
   - Marque a opção "Adicionar Python ao PATH" durante a instalação
2. Baixe e instale o PostgreSQL (https://www.postgresql.org/download/windows/)
3. Baixe e instale o Git (https://git-scm.com/download/win)

### 2. Clonar o Repositório
```powershell
git clone https://github.seu-repositorio.com/prova_teste.git
cd prova_teste
```

### 3. Configurar Ambiente Virtual
```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
.\venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 4. Configurar Banco de Dados PostgreSQL
1. Abra o pgAdmin ou SQL Shell
2. Crie o banco de dados:
```sql
CREATE DATABASE prova_db;
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE prova_db TO seu_usuario;
```

### 5. Configurar Variáveis de Ambiente
1. Copie o arquivo `.env.example` para `.env`
2. Edite o `.env` com suas credenciais

### 6. Preparar Projeto Django
```powershell
# Realizar migrações
python manage.py makemigrations
python manage.py migrate

# Criar usuário admin (opcional)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## Instalação em Linux (Ubuntu/Debian)

### 1. Preparação do Ambiente
```bash
# Atualizar repositórios
sudo apt update

# Instalar dependências
sudo apt install -y python3-pip python3-venv postgresql postgresql-contrib git

# Verificar versões
python3 --version
psql --version
```

### 2. Clonar Repositório
```bash
git clone https://github.seu-repositorio.com/prova_teste.git
cd prova_teste
```

### 3. Configurar Ambiente Virtual
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 4. Configurar Banco de Dados PostgreSQL
```bash
# Acessar PostgreSQL
sudo -u postgres psql

# Criar banco de dados
CREATE DATABASE prova_db;
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE prova_db TO seu_usuario;
\q
```

### 5. Configurar Variáveis de Ambiente
```bash
# Copiar arquivo de configuração
cp .env.example .env

# Editar configurações
nano .env
```

### 6. Preparar Projeto Django
```bash
# Realizar migrações
python manage.py makemigrations
python manage.py migrate

# Criar usuário admin (opcional)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## Instalação em macOS

### 1. Preparação do Ambiente
1. Instalar Homebrew (se não tiver)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Instalar dependências
```bash
# Instalar Python
brew install python

# Instalar PostgreSQL
brew install postgresql

# Instalar Git
brew install git
```

### 2. Clonar Repositório
```bash
git clone https://github.seu-repositorio.com/prova_teste.git
cd prova_teste
```

### 3. Configurar Ambiente Virtual
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 4. Configurar Banco de Dados PostgreSQL
```bash
# Iniciar serviço PostgreSQL
brew services start postgresql

# Acessar PostgreSQL
psql postgres

# Criar banco de dados
CREATE DATABASE prova_db;
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE prova_db TO seu_usuario;
\q
```

### 5. Configurar Variáveis de Ambiente
```bash
# Copiar arquivo de configuração
cp .env.example .env

# Editar configurações
nano .env
```

### 6. Preparar Projeto Django
```bash
# Realizar migrações
python manage.py makemigrations
python manage.py migrate

# Criar usuário admin (opcional)
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

## Solução de Problemas
- Verifique se todas as dependências estão instaladas
- Confirme as configurações do banco de dados no arquivo `.env`
- Certifique-se de estar com o ambiente virtual ativado
- Consulte a documentação do projeto em caso de dúvidas

## Dependências
- Ver arquivo `requirements.txt` para lista completa de pacotes
