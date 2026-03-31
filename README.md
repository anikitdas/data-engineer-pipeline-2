# Data Engineering Pipeline

## Stack
- Apache Spark
- Delta Lake
- ScyllaDB
- Airflow
- Docker

## Run
docker-compose up --build

## Flow
Data Generator → Delta Lake → Spark → ScyllaDB (Airflow Orchestrated)

## Features
- Deduplication
- Data validation
- Aggregation
- Scalable architecture