[![Circle CI](https://circleci.com/gh/NekoTashi/todolist.svg?style=svg)](https://circleci.com/gh/NekoTashi/todolist)

# TODO list App
API Rest app to manage task lists


## How to run
```
0. install python2 and virtualenvwrapper
1. mkvirtualenv todolistapi
2. cdvirtualenv
3. cd todo
4. pip install -r requirements.txt
5. python manage.py migrate
6. python manage.py createsuperuser  # Optional
7. python manage.py runserver
```


## Endpoints
### User endpoints
URL: `/accounts/`

DESCRIPTION: Create a user

METHOD: POST

DATA:

* username
* password
* email


URL: `/accounts/api-token-auth/`

DESCRIPTION: Get the user token auth

METHOD: POST

DATA:

* username
* password


### Task endpoints
URL: `/todo/tasks/`

DESCRIPTION: Get all user tasks

METHOD: GET


URL: `/todo/tasks/`

DESCRIPTION: Create a user task

METHOD: POST

DATA:

* name


URL: `/todo/tasks/<PUT TASK PK HERE>/`

DESCRIPTION: Update a user task

METHOD: PATCH

DATA:

* name
* checked


## Live sample
### ENDPOINTS
#### Create a user
```
curl -v -X POST http://localhost:8000/accounts/ \
	-H 'Content-type: application/json' \
	-d '{"username":"foo","password":"bar","email":"foo@bar.com"}' \
	| python -m json.tool
```

#### Get token auth
```
curl -v -X POST http://localhost:8000/accounts/api-token-auth/ \
	-H 'Content-type: application/json' \
	-d '{"username":"foo","password":"bar"}' \
	| python -m json.tool
```

#### Create a user task
```
curl -v -X POST http://localhost:8000/todo/tasks/ \
	-H 'Content-type: application/json' \
	-H 'Authorization: Token <PUT TOKEN AUTH HERE>' \
	-d '{"name":"test task name"}' \
	| python -m json.tool
```

#### Get all user tasks
```
curl -v -X GET http://localhost:8000/todo/tasks/ \
	-H 'Content-type: application/json' \
	-H 'Authorization: Token <PUT TOKEN AUTH HERE>' \
	| python -m json.tool
```

#### Check or uncheck a user task (this case we check a user task)
```
curl -v -X PATCH http://localhost:8000/todo/tasks/<PUT TASK PK HERE>/ \
	-H 'Content-type: application/json' \
	-H 'Authorization: Token <PUT TOKEN AUTH HERE>' \
	-d '{"checked":true}' \
	| python -m json.tool
```