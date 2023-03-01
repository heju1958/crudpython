<h1 align="center">
	<img src='https://www.svgrepo.com/show/142693/notes.svg' alt='Icone de anotações' width='30px' height='30px'/> CRUD Python Employees

## Tecnologias utilizadas:

> Foi desenvolvida com as tecnologias Python, Django, Django Rest Framework e o banco de dados PostgreSQL.

## Links:

``Documentação (swagger):``
```
https://api-crud-employees.onrender.com/docs/swagger/
```

``Deploy:``

Sua url base é 

```
https://api-crud-employees.onrender.com
```

## Endpoints:

A API tem 6 endpoints, sendo em volta do usuário - podendo cadastrar seu perfil, realizar login, atualizar seus dados e deletar seu perfil, e tendo a diferença entre os usuários comuns e os administradores.

<h2>
	Endpoints necessitam de autenticação:
</h2> 

E necessário passar um token para realizar uma requisição bem sucedida nos seguintes endpoints:

<h2 align = "center">
	Criação de Usuário
</h2>

``POST -> api/users/ - FORMATO DA REQUISIÇÃO - usuário comum``

```json
{
	"username": "Empregado 1",
	"email": "empregado1o@gmail.com",
	"password": "1234"
}
```

``FORMATO DA RESPOSTA - STATUS 201 - CREATED``

```json
{
	"id": "5a16e3af-f38a-44e7-b977-aaed4b62479d",
	"is_superuser": false,
	"username": "Empregado 1",
	"email": "empregado1o@gmail.com",
	"is_adm": false
}
```

<br/>

``POST -> api/users/ - FORMATO DA REQUISIÇÃO - usuário administrador``

```json
{
	"username": "SuperUser",
	"email": "superuser@gmail.com",
	"password": "1234",
	"is_adm": "True"
}
```

``FORMATO DA RESPOSTA - STATUS 201 - CREATED``

```json
{
	"id": "532e1791-5a2f-44bd-b7db-08fcbea6a29d",
	"is_superuser": true,
	"username": "SuperUser",
	"email": "superuser@gmail.com",
	"is_adm": true
}
```
