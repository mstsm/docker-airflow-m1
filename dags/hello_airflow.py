from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


# DAGを作る
default_args = {
    "owner": "mmummu",
    "depends_on_past": False,
    "start_date": datetime(2018, 4, 21, 10, 0, 0),
    "schedule_interval": timedelta(days=1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("my_first_dag", default_args=default_args)

# DAGと紐づくタスクを作る
t1 = BashOperator(task_id="t1", bash_command="echo t1", dag=dag)

t2 = BashOperator(task_id="t2", bash_command="exit 1", retries=3, dag=dag)

t3 = BashOperator(
    task_id="t3",
    bash_command='echo "{{ params.greeting }}"',
    params={"greeting": "Hello, AirFlow!"},
    dag=dag,
)

t4 = BashOperator(task_id="t4", bash_command="echo t4", dag=dag)

# タスク間に依存関係を定義する
t2.set_upstream(t1)
t3.set_upstream(t1)
t4.set_upstream([t2, t3])
