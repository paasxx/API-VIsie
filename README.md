# API-VIsie

"Um site usando ReactJS e API REST em Python, usando Flask, que fornece um sistema CRUD (Create, Read, Update and Delete) com banco de dados SQLite para controle de funcionários"


## Como Começar

Siga os passos abaixo para executar o projeto.

### Pré-requisitos

1. Node.js para o frontend React
2. requirements.txt 

### Tecnologias

1. React (Front End)
2. Python 🐍 
3. Flask 🐍 (Backend)
3. SQLite (Banco de Dados)
. Postman (Teste externo Endpoints)

### Instalação


1. Clone este repositório em sua máquina local:

```bash
git clone https://github.com/paasxx/API-VIsie.git
```

2. Navegue até o diretório do projeto:

```bash
cd API-VIsie
```

2.1 Para instalar as bibliotecas necessários do arquivo requirements.txt pode-se criar um ambiente virtual na raiz do projeto, dentro da pasta API-VIsie, o comando no (Mac OS) é.

```bash
python3 -m venv venv
```
2.2 Para ativar o ambiente virtual:

```bash
source venv/bin/activate
```
2.4 Instale o React Router Dom:

```bash
npm i react-router-dom --save
```
2.5 Instale o Axios:

```bash
npm install axios --save
```

3. Execute a API na riaz do projeto e depois o Front End:

```bash
flask run
```

```bash
cd myreactdev
```

```bash
npm start
```

4. O site deve carregar automaticamente no chrome senão no prompt é fornecido o link: `http://localhost:3000/`:


```

A API estará acessível em `http://127.0.0.1:5000/`.

### Endpoints da API

| Método   | Endpoint                    | Descrição                                      |
|----------|-----------------------------|------------------------------------------------|
| GET      | /                           | Hello World                                    |
| GET      | /listusers                  | Lista de Todos os usuários                     |
| DELETE   | /userdelete/<id>            | Deleta o usuário                               |
| GET      | /userdetails/<id>           | Recupera informações detalhadas de um usuário  |
| PUT      | /userupdate/<id>            | Atualiza os dados do usuário                   |
| POST     | /useradd                    | Adiciona um novo usuário ao banco de dados     |


### Parâmetros de entrada para Endpoints da API

Exemplo de parâmetro de entrada para os métodos PUT e POST no formato .json

```json
{
    "name": "Pedro André Aguiar da Silveira",
    "rg": "14496948",
    "cpf": "01587181608",
    "data_nascimento": "1992-01-31",
    "data_admissao": "2019-04-08"
}
```
