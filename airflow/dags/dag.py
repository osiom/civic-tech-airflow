import logging

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

logger = logging.getLogger("airflow.task")

def greet():
    logger.info("Hello, welcome to the Civic Tech Airflow environment!")

with DAG(
    owner_links={"osiom": "https://github.com/osiom/matteoosio.me"},
    dag_id="civic_tech_greeting",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,  # No automatic scheduling; manual trigger
    catchup=False,
) as dag:

    # Define the task
    greeting_task = PythonOperator(
        task_id="greet_task",
        python_callable=greet,
    )

    greeting_task
