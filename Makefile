.PHONY: lint isort

# Run flake8 for Python code linting
lint:
	flake8 airflow/

# Run isort to automatically sort imports
isort:
	isort airflow/

# Run both linting and import sorting checks
check: lint isort

## build-local: build local Airflow image
build-local:
	docker-compose build

## spinup-local: spin up local machine
spinup-local:
	docker-compose up -d

## terminate-local: terminate local environment
terminate-local:
	docker-compose down