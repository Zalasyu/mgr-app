## Setup Development Environment
dev:
	@export FLASK_APP=app.main.py
	@export FLASK_ENV=development
	@cd app && flask run

## Open Browser to localhost:5000
open:
	@open http://localhost:5000