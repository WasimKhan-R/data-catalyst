# 📊 Data Catalyst – Scalable Data Processing Platform  

## 🚀 Summary  
Data Catalyst is a **Django + DRF + Celery + Redis + PostgreSQL + Docker** project for handling **large Excel data ingestion** (up to 1M+ company records).  
It processes files in the **background with Celery workers** and provides **filter & search APIs** for efficient querying.  

---

# 🐳 Project Setup with Docker  

Follow the steps below to set up and run the project locally using Docker.

## 1. Clone the repository
git clone https://github.com/WasimKhan-R/data-catalyst.git

## 2. Navigate to the project directory
cd data_catalyst

## 3. Build the Docker images
docker-compose build

## 4. Start the Docker containers
docker-compose up -d

## 5. Run migrations
docker-compose exec django python manage.py migrate

## 6. Create a superuser (optional, for admin access)
docker-compose exec django python manage.py createsuperuser

---

## 🔗 Access the App
Django App: http://localhost:8000
API Endpoint Example: http://localhost:8000/api/upload/

---

## 📦 Example Dataset
A sample 10,000 company dataset is included:
📂 catalyst_10000.csv
