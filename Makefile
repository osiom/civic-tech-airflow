## build-local: build local Airflow image
build-local:
	docker-compose build

## spinup-local: spin up local machine
spinup-local:
	docker-compose up -d

## terminate-local: terminate local environment
terminate-local:
	docker-compose down