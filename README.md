# Projeto Auto ClickIP Local

Bem-vindo ao repositório do **Auto ClickIP Local**! Este projeto tem como objetivo automatizar tarefas de rede utilizando Flask, Flask-Migrate, Netmiko, PyEZ, ipaddress e outras bibliotecas.

## 📌 Funcionalidades
- Integração com dispositivos de rede via **NETCONF** e **RESTCONF**
- Gerenciamento de VLANs e prefixos de rede
- Criação automática de usuário administrador
- Validação de endereços IP e prefixos
- Flask com Flask-Migrate para gestão de banco de dados
- Ambiente virtual gerenciado com Makefile

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Flask** (framework web)
- **Flask-Migrate** (migração de banco de dados com SQLAlchemy)
- **Netmiko / PyEZ** (conexão com equipamentos de rede)
- **ipaddress** (manipulação de endereços IP)
- **WTForms** (validação de formulários)
- **Docker Compose** (opcional para conteinerização)

## 🚀 Como Rodar o Projeto

### 1️⃣ Clonar o Repositório
```bash
https://github.com/NocDevDatacenter/auto.clickip.local.git
cd auto-clickip-local
```

### 2️⃣ Criar o Ambiente Virtual
```bash
make venv
```

### 3️⃣ Instalar as Dependências
```bash
make install
```

### 4️⃣ Configurar as Variáveis de Ambiente
Crie um arquivo **.env** na raiz do projeto e defina suas credenciais:
```ini
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
DEVICE_TYPE=juniper
HOSTNAME=192.168.1.1
USERNAME=meu_usuario
PASSWORD=minha_senha
PORT=22
```

### 5️⃣ Rodar a Aplicação
```bash
make run
```
Acesse **http://127.0.0.1:5000** no navegador.

## 📂 Estrutura do Projeto
```
app/
├── __init__.py
├── models/
├── controllers/
├── static/
├── templates/
├── config.py
├── create_admin.py
└── sandbox.py
```

## 🐍 Rodando Migrações do Banco de Dados
Caso faça alterações no modelo de dados, execute:
```bash
flask db migrate -m "atualizando tabelas"
flask db upgrade
```

## 📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar! 🎉

