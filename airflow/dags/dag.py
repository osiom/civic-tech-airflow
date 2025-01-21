from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def greet():
    print("Hello, welcome to the Civic Tech Airflow environment!")

with DAG(
    dag_id="civic_tech_greeting",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,  # No automatic scheduling; manual trigger
    catchup=False,
) as dag:

    # Define the task
    greeting_task = PythonOperator(
        task_id="greet_task",
        python_callable=greet,
    )

    greeting_task
