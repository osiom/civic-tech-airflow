# Use the Apache Airflow 2.9.2 image with Python 3.10
FROM apache/airflow:2.9.2-python3.10

# Install additional Python packages if needed
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Change the working directory
WORKDIR /opt/airflow

# Copy DAGs and plugins into the container
COPY dags /opt/airflow/dags

# Set the Airflow user
USER airflow
