VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

.PHONY: venv install run clean flake
.PHONY: mig init status reset upgrade downgrade

venv:
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip > /dev/null
	@echo "Pip updated."
	@echo "Virtual environment created in $(VENV)"

install: venv
	@$(PIP) install -r requirements.txt  --no-cache-dir
	@echo "Dependencies installed."

run:
	@PYTHONDONTWRITEBYTECODE=1 FLASK_ENV=development FLASK_APP=run.py $(PYTHON) -m flask run --debug --reload
	@echo "Application is running."

clean:
	@find . -type d \( -name "__pycache__" -o -name ".pytest_cache" \) -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@rm -rf $(VENV)
	@echo "Cache and $(VENV) successfully removed."

flake:
	@echo 'Checking flake8...'
	@flake8 --exclude $(VENV)

migrate:
	flask db current
	flask db migrate -m "automatic migration"
	flask db upgrade
	
init:
	flask db init

status:
	flask db current
	flask db history

reset:
	rm -rf migrations/
	flask db init
	flask db migrate -m "initial migration after reset"
	flask db upgrade