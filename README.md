# Data Engineering Pipeline using Airflow, Spark, and ScyllaDB

## Overview

This project demonstrates an end-to-end data engineering pipeline built using Apache Airflow, Apache Spark (simulated locally), and ScyllaDB. The pipeline is fully containerized using Docker Compose and processes customer transaction data from ingestion to storage.

## Architecture

The pipeline follows this flow:

Data Generation → Data Cleaning (Delta Layer) → Transformation → ScyllaDB Storage
Orchestrated by Apache Airflow

## Components

### 1. Data Generation

A Python script generates synthetic customer transaction data with:

* Unique transaction IDs
* Random customer IDs
* Transaction amounts
* Timestamps
* Merchant names

It also includes real-world scenarios such as:

* Duplicate transactions
* Invalid (negative/zero) values

---

### 2. Data Cleaning (Delta Layer)

The raw data is cleaned by:

* Removing duplicate records
* Filtering invalid transactions
* Saving processed data into a structured data layer

---

### 3. Data Transformation

The transformation stage performs:

* Extraction of transaction date from timestamp
* Aggregation of daily transaction totals per customer
* Preparation of final dataset for database storage

---

### 4. Data Loading (ScyllaDB)

The processed data is loaded into ScyllaDB with:

* Customer ID as partition key
* Transaction date as clustering key
* Daily total as aggregated value

---

### 5. Workflow Orchestration (Airflow)

Apache Airflow is used to:

* Define task dependencies
* Automate execution of each stage
* Monitor pipeline execution
* Handle retries and failures

The DAG includes:

* Data generation
* Data cleaning
* Transformation
* Database loading

---

## Technologies Used

* Apache Airflow (Workflow Orchestration)
* Apache Spark (Transformation Logic - simulated locally)
* ScyllaDB (NoSQL Database)
* Docker Compose (Containerization)
* Python (Data Processing)

---

## Features

* Fully containerized pipeline
* Modular ETL design
* Automated workflow using DAGs
* Data validation and cleaning
* End-to-end execution with monitoring

---

## How to Run

1. Start all services using Docker Compose
2. Open Airflow UI in browser
3. Trigger the ETL pipeline DAG
4. Monitor execution in Graph View

---

## Output

The pipeline produces:

* Cleaned transaction data
* Aggregated daily customer totals
* Stored records in ScyllaDB

---

## Key Learnings

* Building ETL pipelines using Airflow
* Handling containerized environments
* Data cleaning and transformation techniques
* Debugging distributed systems
* Workflow orchestration and monitoring

---

## Conclusion

This project demonstrates a complete data pipeline from raw data ingestion to processed storage using modern data engineering tools. It highlights the importance of orchestration, data quality, and scalable design.
