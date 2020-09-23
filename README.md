# KaBuM - Flask API Rest

API Rest feito em Flask para listagem de produtos da KaBuM.

Segue desenho esquemático com camadas arquiteturais: [ACESSE AQUI](https://drive.google.com/file/d/17vmO5qaM9u-DEz7IX9IWUl4HUgQuKGjU/view?usp=sharing)

**flask_restful**: Uma lib que facilita o controle dos dados que serão renderizados na resposta.- Com o recurso marshal_with é possível definir um retorno padrão para sua resposta podendo "excluir" os dados que você não quer que retorne para o usuário.

**flask.views.MethodView**: É uma das `Pluggable View` que o Flask nos disponibiliza. Inspirada nas `generics views` do Django, o MethodView é uma view baseada em classe que disponibiliza métodos correspondentes aos métodos HTTP e a possibilidade de aproveitamento de rotas para diversas requisições.

## Começando

Para execução do projeto será necessário a instalação do [PYTHON](https://www.python.org/)

## Desenvolvimento

Para iniciar o projeto ou o desenvolvimento de melhorias basta clonar o projeto do GitHub num diretório de sua preferência:

```python
  cd "diretorio de sua preferencia"
  git clone https://github.com/pedroimpulcetto/kabum-flask.git
```

## Inicialização

Após o python instalado e o projeto clonado, será necessário criar uma virtual env(`venv`) para instalar as depedências sem conflito com seu sistema operacional.

- `python3 -m venv venv`

Ative sua venv: `source venv/bin/activate`

Agora instalaremos todas as dependências para que nosso projeto consiga rodar.
Instale o `requirements.txt` que encontra-se na raiz do projeto

- `pip install -r requirements.txt`

Crie o banco de dados e as tabelas:

- `python run.py db migrate`
- `python run.py db upgrade`

Inicie o server

- `python run.py runserver`

acesse http://127.0.0.1:5000/ 

## Features

A principal função desse projeto é a listagem de produtos `mocks` da KaBuM utilizando as ferramentas `flask_restful` e `flask.views.MethodView` do framework Flask.

O projeto está subdividido em 2(duas) partes:
  - **PARTE 1 -** na rota "/" acessamos uma listagem de produtos criados e armazenados em um banco de dados SQLite.
  - **PARTE 2 -** na rota "/kabum" acessamos uma listagem contendo 3(três) protudos disponibilizados.

Utilizei para desenvolvimento do projeto os conceitos dos pacotes:
    - *flask*,
    - *flask_restful*,
    - *flask_sqlalchemy*, 
    - *flask_script*, 
    - *flask_migrate*

Implementei a utilização de **ORM's** para controle e manipulação dos dados nas consultas do banco de dados.
Utilizei `@dataclass` para simplificação e modelagem da estrutura dos models.


### PARTE 1

Nessa parte do projeto foi feito: 

A integração com um banco de dados do tipo *SQLite* e o modelo desenvolvido para essa parte segue o seguinte formato:

```python
  product = {
    "product_id": int,
    "product_name": str,
    "price": float
  }
```

Na rota "/" temos acesso aos métodos HTTP *"GET"* e *"POST".*
  - Método GET trará a listagem de todos os produtos existentes no banco de dados
  - Método POST é possível incluir um novo produto
    *payload válido seria*: 
```json
{
  "product_name": str,
  "price": float
}
```

E na rota "/<<int:product_id>>" temos acesso aos métodos HTTP *"GET"*, *"PUT"* e *"DELETE"*.
Podendo executar, respectivamente, cada um deles para retornar o registro de um produto, alterar um produto e deletar um produto.

### PARTE 2

Nesse segunda parte do projeto realizei a listagem de todos os 3 (três) produtos "mockados" nas rotas disponibilizadas para o teste.

Podemos acessar essa listagem na rota "*/kabum*" que tem acesso ao Método HTTP *"GET"* retornando a listagem dos produtos com um "cabeçalho" contendo a data da request, o total de registro e os resultados da listagem, ficando assim:

```json
{
  "date": "Wed, 23 Sep 2020 14:53:49 GMT",
  "quantity_total": 3,
  "results": [
    {},
    {},
    {}
  ]
}
```

E temos também o acesso à rota "*/kabum/<<int:codigo>>*" com os Método *"GET"* e *"DELETE"*, podendo executar, respectivamente, cada um deles para listar o produto específico e deletar o registro.


## Autor

#### **Pedro Impulcetto**

[![Linkedin Badge](https://img.shields.io/badge/-pedroimpulcetto-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/pedroimpulcetto/)](https://www.linkedin.com/in/pedroimpulcetto/)
[![YouTube Badge](https://img.shields.io/badge/-PedroImpulcetto-ff0000?style=flat&logo=YouTube&logoColor=white&link=https://www.youtube.com/channel/UCsnD5AhrIq7BvKvZFKLT-pQ?view_as=subscriber)](https://www.youtube.com/channel/UCsnD5AhrIq7BvKvZFKLT-pQ?view_as=subscriber)
[![Gmail Badge](https://img.shields.io/badge/-pedro.impulcetto@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:pedro.impulcetto@gmail.com)](mailto:pedro.impulcetto@gmail.com)

Repositório GitHub: (https://github.com/pedroimpulcetto)
