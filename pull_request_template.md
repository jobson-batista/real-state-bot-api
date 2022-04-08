## Status
**READY/IN DEVELOPMENT/HOLD**

## Descrição
Algum texto descrevendo os objetivos gerais dos commits da pull request.

## TO DO
- [ ] Testes
- [ ] Documentação

## Sobre o Deploy
Informações sobre o Deploy. Por exemplo: configuação específica de variáveis de ambiente, etc.

## Passos para reproduzir ou testar
Sequência de passos.

```sh
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
```
