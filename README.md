# Project Setup

Follow the steps below to set up and run the project locally using Docker.

## 1. Clone the repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/WasimKhan-R/data-catalyst.git
```

## 2. Navigate to the project directory

```bash
cd data_catalst
```

## 3. Build the Docker images

```bash
docker-compose build
```

## 4. Start the Docker containers

```bash
docker-compose up -d
```

## 5. Run migrations

```bash
docker-compose exec django python manage.py migrate
```
