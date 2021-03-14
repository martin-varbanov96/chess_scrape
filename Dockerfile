FROM puckel/docker-airflow:1.10.9

RUN mkdir app
COPY . app
