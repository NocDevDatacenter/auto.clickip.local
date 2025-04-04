VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

.PHONY: venv install run clean flake
.PHONY: mig init status reset upgrade downgrade

################### ################### ################### ################### ################### 
#### DEPLOYMENT ### #### DEPLOYMENT ### #### DEPLOYMENT ### #### DEPLOYMENT ### #### DEPLOYMENT ### 
################### ################### ################### ################### ################### 

venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV); \
		$(PIP) install --upgrade pip > /dev/null; \
		echo "Pip updated."; \
	else \
		echo "Virtual environment already exists."; \
	fi
	@sleep 5

install: venv
	@echo "Dependencies installed."
	@$(PIP) install -r requirements.txt  --no-cache-dir > /dev/null

run:
	@export PYTHONDONTWRITEBYTECODE=1 FLASK_APP=run.py && $(PYTHON) -m flask run --debug --host=0.0.0.0

clean:
	@find . -type d \( -name "__pycache__" -o -name ".pytest_cache" \) -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@rm -rf $(VENV)
	@echo "Cache and $(VENV) successfully removed."

################### ################### ################### ################### ################### 
###### FLAKE ###### ###### FLAKE ###### ###### FLAKE ###### ###### FLAKE ###### ###### FLAKE ###### 
################### ################### ################### ################### ################### 

flake:
	@echo 'Checking flake8...'
	@$(PYTHON) -m flake8 --exclude $(VENV)

################### ################### ################### ################### ################### 
##### MIGRATE ##### ##### MIGRATE ##### ##### MIGRATE ##### ##### MIGRATE ##### ##### MIGRATE ##### 
################### ################### ################### ################### ################### 

migrate:
	@$(PYTHON) -m flask db current
	@$(PYTHON) -m flask db migrate -m "automatic migration"
	@$(PYTHON) -m flask db upgrade
	
mig-init:
	@$(PYTHON) -m flask db init

mig-status:
	@$(PYTHON) -m flask db current
	@$(PYTHON) -m flask db history

mig-reset:
	rm -rf migrations/
	@$(PYTHON) -m flask db init
	@$(PYTHON) -m flask db migrate -m "initial migration after reset"
	@$(PYTHON) -m flask db upgrade

################### ################### ################### ################### ################### 
##### ENDLINE ##### ##### ENDLINE ##### ##### ENDLINE ##### ##### ENDLINE ##### ##### ENDLINE ##### 
################### ################### ################### ################### ################### 