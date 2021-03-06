try:

    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import pandas as pd
    from scrape_player_games import PlayerGamesScraper

except Exception as e:
    print(f"Error: {e}")

def get_montly_chess_com_games(*args, **kwargs):
    player_games_scraper = PlayerGamesScraper()
    player_games_scraper.scrape_last_month_games("funvengeance")

with DAG(
        dag_id="basic_chess_dag",
        schedule_interval="@monthly",
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
    )

