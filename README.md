# API-VIsie

"Um site usando REACT JS e API REST em Python, usando Flask, que forneceum sistema CRUD Create, Read, Update and Delete com banco de dados SQLite para controle de funcionários"


## Como Começar

Siga os passos abaixo para executar o projeto.

### Pré-requisitos

1. Node.js para o frontend React
2. requirents.txt 

### Tecnologias

1. React 🐳
2. Python
3. Flask
3. SQLite
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

3. Execute a API e depois o Front End:

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


5. Para obter o token, vá em `http://localhost:8000/api/token` usando o Postman com o seguinte corpo para o POST:

```json
{
    "username": "admin",
    "password": "adminpass"
}

```

6. Com o token obtido na response acima, utilizamos API Key para autenticação de todos os endpoints, no Postman em Auth.


```json
Example: {
    "Key": "Authorization",
    "Value": "Token ddeeb8b9966e53de79e7519d2cfb4aef9cde87a4"
}


```


A API estará acessível em `http://localhost:8000/api`.

### Endpoints da API

| Método   | Endpoint                    | Descrição                                      |
|----------|-----------------------------|------------------------------------------------|
| GET      | /                           | Detalhes da API                                |
| PUT      | /product/:code             | Atualiza informações do projeto Web            |
| DELETE   | /product/:code             | Altera o status do produto para "excluído"     |
| GET      | /product/:code             | Recupera informações detalhadas de um produto  |
| GET      | /products                   | Lista todos os produtos                        |
| POST     | /product/create            | Adiciona um novo produto ao banco de dados     |
| POST     | /token                      | Obtém o Token de autorização                   |
| POST     | /schema/docs                | Documentação da API                 |


### Parâmetros de entrada para Endpoints da API

Exemplo de parâmetro de entrada para os métodos PUT e POST no formato .json

```json
{
  "code": 20221126,
  "status": "published",
  "imported_t": "2020-02-07T16:00:00Z",
  "url": "https://world.openfoodfacts.org/product/20221126",
  "creator": "securita",
  "created_t": 1415302075,
  "last_modified_t": 1572265837,
  "product_name": "Madalenas quadradas",
  "quantity": "380 g (6 x 2 u.)",
  "brands": "La Cestera",
  "categories": "Lanches comida, Lanches doces, Biscoitos e Bolos, Bolos, Madalenas",
  "labels": "Contem gluten, Contém derivados de ovos, Contém ovos",
  "cities": "",
  "purchase_places": "Braga,Portugal",
  "stores": "Lidl",
  "ingredients_text": "farinha de trigo, açúcar, óleo vegetal de girassol, clara de ovo, ovo, humidificante (sorbitol), levedantes químicos (difosfato dissódico, hidrogenocarbonato de sódio), xarope de glucose-frutose, sal, aroma",
  "traces": "Frutos de casca rija,Leite,Soja,Sementes de sésamo,Produtos à base de sementes de sésamo",
  "serving_size": "madalena 31.7 g",
  "serving_quantity": 31.7,
  "nutriscore_score": 17,
  "nutriscore_grade": "d",
  "main_category": "en:madeleines",
  "image_url": "https://static.openfoodfacts.org/images/products/20221126/front_pt.5.400.jpg"
}
```

### Testes

Para executar testes unitários para a API dentro do contêiner, use o seguinte comando:

Obter o id do container Docker:

```bash
docker ps
```
Rodar o teste:

```bash
docker exec -it container_id python manage.py test
```

### Segurança 

Foi implementada com auxílio do Django Rest Framework a autenticação via token com API Key, que deve ser incorporada no cabeçalho de autorização se estiver testando por exemplo com o Postman.

### Documentação 📚🚀

Documentação completa da API usando o padrão OpenAPI 3.0 acesse:

`http://localhost:8000/api/schema/docs/`
