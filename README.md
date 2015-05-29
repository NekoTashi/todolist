# TODO list App
API Rest app to manage task lists

## How to run
In progress...

## Endpoints
In progress...

## Live testing
### ENDPOINTS
#### Create a user
curl -v -X POST http://localhost:8000/accounts/ \
	-H 'Content-type: application/json' \
	-d '{"username":"foo","password":"bar","email":"foo@bar.com"}' \
	| python -m json.tool

# Get token auth
curl -v -X POST http://localhost:8000/accounts/api-token-auth/ \
	-H 'Content-type: application/json' \
	-d '{"username":"foo","password":"bar"}' \
	| python -m json.tool

# Create a user task
curl -v -X POST http://localhost:8000/todo/tasks/ \
	-H 'Content-type: application/json' \
	-H 'Authorization: Token <PUT A TOKEN AUTH HERE>' \
	-d '{"name":"foo bar task"}' \
	| python -m json.tool

# Get all user tasks
curl -v -X GET http://localhost:8000/todo/tasks/ \
	-H 'Content-type: application/json' \
	-H 'Authorization: Token <PUT A TOKEN AUTH HERE>' \
	| python -m json.tool

# Check or uncheck a user task (this case we check a user task)
curl -v -X PATCH http://localhost:8000/todo/tasks/<PUT A TASK PK HERE>/ \
	-H 'Content-type: application/json' \
	-H 'Authorization: Token <PUT A TOKEN AUTH HERE>' \
	-d '{"checked":true}' \
	| python -m json.tool