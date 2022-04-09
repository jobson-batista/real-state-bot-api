# Real State Bot PB API - RSBPB ![enter image description here](https://img.shields.io/badge/version-1.0.0-yellowgreen)
### API REST para gerenciar buscas automáticas por imóveis

### URL do projeto implamantado no Heroku:
`https://real-state-bot-pb-api.herokuapp.com/`

### ✅ Status do Projeto
<h4 align="center"> 🚧 Em desenvolvimento ... 🚧 </h4>

### ✅ Requisitos para rodar o projeto
- [Python 3.x](https://www.python.org/downloads/) 

### ✅ Features

 - [x] Buscar último imóvel cadastrado na olx
 - [x] Filtrar busca por cidade e bairros
 - [x] Enviar anúncio para o telegram
 - [x] Obter todos os bairros de uma cidade

### ✅ Passos para executar o projeto localmente

- Entrar na raiz do projeto.
- Criar um ambiente virtual com python usando o comando:`python3 -m venv env`
- Ativar o ambiente virtual
	- No Linux: `source env/bin/activate`
	- No Windows: `env/Scripts/Activate`
- Instalar as dependências: `pip install -r requirements.txt`
- Definir uma variável de ambiente
	- No linux: `export FLASK_APP=app`
	- No CMD: `set FLASK_APP=app`
	- No Powershell: `$env:FLASK_APP = app`
- Por fim executar o comando: `flask run`

### ✅ Principais Endpoints

#### Gerenciamento de buscas

|*Operação*|*HTTP Method*| *URI*|
|--|--|--|
| Buscar último imóvel em João Pessoa | GET | /search
| Buscar último imóvel da cidade {city} e bairro {district} | GET | /search?city=joao-pessoa&district=aeroclube
| Obter lista de bairros de uma cidade | GET | /{city}/districts
| Enviar um anúncio para o grupo no telegram | POST | /sendAd
