# civic-tech-airflow

## Customizing the Environment

This image is based on apache/airflow:2.9.2-python3.10

- **Adding Python Libraries**:  

To update the requirements please add the dedicated package to the correct `.in` file.

The `requirements.txt` and `requirements-dev.txt` files are created from using pip-tools using a Docker container. By convenience, you can use this command to update these files:

Execute from CLI this command to generate the requirements file.

```bash
docker build --file Dockerfile.requirements --target export-requirements --output type=local,dest=. .
```

Summarising, to add additional Python libraries to your Airflow environment:
  1. Add the required dependencies to the `requirements.airflow.in` file.
  2. Rebuild the `.txt` requirement files with the following command:
     ```bash
     docker build --file Dockerfile.requirements --target export-requirements --output type=local,dest=. .
     ```
  3. Spinup again the environment using the Make command

- **Adding DAGs**:  
  Place your custom DAG files in the `airflow/dags` directory. They will be automatically loaded by the Airflow webserver.

- **Modifying Configuration**:  
  To customize the Airflow configuration:
  1. Update environment variables in the `.env` file for Airflow.
  2. Alternatively, modify the `airflow.cfg` file directly in the `airflow-webserver` container by opening an interactive shell:
     ```bash
     docker-compose exec airflow-webserver bash
     ```
     Navigate to the `airflow.cfg` file, make the necessary changes, and restart the container.

- **Code Quality Check**:  
  Before pushing a PR there's the possibility to perform basic PEP checks by running:
  ```bash
  make check
  ```
  This command will perform [isort](https://pycqa.github.io/isort/) and [flake8](https://flake8.pycqa.org/en/latest/) checks on the `airflow/` folder to make sure code standards are followed.
