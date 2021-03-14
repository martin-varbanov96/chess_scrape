try:

    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import pandas as pd

except Exception as e:
    print(f"Error: {e}")

def get_montly_chess_com_games(*args, **kwargs):
    # TODO: get chess.com data
    pass


with DAG(
        dag_id="basic_chess_dag",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        },
        catchup=False) as f:

    first_function_execute = PythonOperator(
        task_id="get_montly_chess_com_games",
        python_callable=get_montly_chess_com_games,
        provide_context=True,
        # TODO: add option for users
        # op_kwargs={"name":"Soumil Shah"}
    )

