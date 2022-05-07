from datetime import datetime, timedelta
from email.policy import default
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator

from scripts import func

default_args = {
    "owner": 'chris123',
    'retires': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='etl_covid_case',
    schedule_interval="@daily",
    start_date=datetime(2022, 5, 5),
    default_args=default_args
) as dag:
    
    start = DummyOperator(
        task_id="Start"
    )
    
    api_to_mysql = PythonOperator(
        task_id="api_to_mysql_task",
        python_callable=func.api_to_mysql,
        op_kwargs={"url": 'https://covid19-public.digitalservice.id/api/v1/rekapitulasi_v2/jabar/harian?level=kab'}
    )
    
    mysql_to_postgres = PythonOperator(
        task_id="mysql_to_postgres_task",
        python_callable=func.mysql_to_postgres,
    )
    
    create_table_task = PostgresOperator(
        task_id="create_table_task",
        postgres_conn_id='postgres_engine',
        sql='./sql/create_table.sql'
    )
    
    populate_dim_table_task = PostgresOperator(
        task_id='populate_dim_table_task',
        postgres_conn_id='postgres_engine',
        sql='./sql/populate_dim_table.sql'
    )
    
    dim_case_task = PythonOperator(
        task_id='dim_case_task',
        python_callable=func.dim_case_table
    )
    
    populate_fact_table_task = PostgresOperator(
        task_id="populate_fact_table_task",
        postgres_conn_id='postgres_engine',
        sql='./sql/populate_fact_table.sql'
    )

start >> api_to_mysql >> mysql_to_postgres >> create_table_task >> populate_dim_table_task >> dim_case_task >> populate_fact_table_task
