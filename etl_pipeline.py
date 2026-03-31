from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "anikit",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="etl_pipeline",
    default_args=default_args,
    schedule=None,
    catchup=False,
) as dag:

    generate_data = BashOperator(
        task_id="generate_data",
        bash_command="python3 /scripts/generate_data.py",
    )

    load_to_delta = BashOperator(
        task_id="load_to_delta",
        bash_command="python3 /scripts/load_to_delta.py",
    )

    spark_etl = BashOperator(
        task_id="spark_etl",
        bash_command="python3 /scripts/spark_job.py",
    )

    load_to_scylla = BashOperator(
        task_id="load_to_scylla",
        bash_command="python3 /scripts/scylla_loader.py",
    )

    generate_data >> load_to_delta >> spark_etl >> load_to_scylla
