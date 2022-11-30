## Setup Development Environment
dev:
	@export FLASK_APP=app.main.py
	@export FLASK_ENV=development
	@cd app && flask run
