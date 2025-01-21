import logging
from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator

from airflow import DAG

logger = logging.getLogger("airflow.task")

default_args = {
    "owner": "osiom",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 1),
    "email": ["matteo.osio1992@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}


def greets():
    logger.info("Hello, welcome to the Civic Tech Airflow environment!")


with DAG(
    dag_id="civic-tech_greetings",
    default_args=default_args,
    schedule_interval=None,  # No automatic scheduling; manual trigger
    catchup=False,
    tags=["general-purpose"],
) as dag:
    # Define the task
    greeting_task = PythonOperator(
        task_id="greeting_task",
        python_callable=greets,
    )

    greeting_task
