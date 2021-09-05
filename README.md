https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

# setup1

```bash
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

```bash
docker-compose up
docker-compose run airflow-worker airflow info
```

# setup2

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.3/airflow.sh'
chmod +x airflow.sh

/airflow.sh info
```

# web

http://localhost:8080

- id : airflow
- pass : airflow

# 削除

```bash
docker-compose down --volumes --rmi all
```
