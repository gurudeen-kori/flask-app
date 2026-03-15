# MyApp: Flask + MySQL + Redis Docker Stack
**Prepaired by Gurudeen kori**
## Overview

This is a **minimal 3-service stack**:

- **Web App:** Python Flask  
- **Database:** MySQL  
- **Cache:** Redis  

The web app connects to MySQL and Redis, and displays a simple message on the home page.
****
---

## Folder Structure


myapp/

│

├─ docker-compose.yml

│

└─ web/

├─ Dockerfile

├─ requirements.txt

└─ app.py


---

## Prerequisites

- [Docker](https://www.docker.com/get-started) installed  
- [Docker Compose](https://docs.docker.com/compose/install/) installed  

---
# docker file base image 
```
python:3.11-slim
```
# web app environment 
    environment:
      - DATABASE_URL=mysql+pymysql://root:test@123@mysql:3306/mydb
      - REDIS_URL=redis://cache:6379
# Ports
`"5000:5000"`

## Requirement
```
Flask==2.3.5
SQLAlchemy==2.0.23
PyMySQL==1.1.0
redis==5.3.2
```
# database environment variable 
environment:
      MYSQL_ROOT_PASSWORD: test@123
      MYSQL_DATABASE: mydb
# Ports 
`"3306:3306"`

## Quick Start

1. **Clone the repository** (or copy files):

```bash
git clone <repo-url>
cd myapp
```
**Start all services:**
```
docker-compose up --build
```
Open the app in a browser:

http://localhost:5000

# You should see:

Hello World! Redis says: Hello Redis!

Stop services:
```
docker-compose down
```
# Notes

The Flask app includes retry logic to wait for MySQL and Redis to be ready.

To rebuild the images after changes:
```
docker-compose up --build
```

# Flask MySQL Redis App

## Overview
This is a simple multi-service app using **Flask**, **MySQL**, and **Redis** running in Docker.  
The app demonstrates a basic web application that connects to a database and cache, suitable for learning Docker Compose and containerized stacks.

## Components

### Flask
- Python web framework used to build the app.
- Serves a web page at the `/` endpoint.
- Reads data from Redis and displays it.
- Connects to MySQL to verify the database is ready.
- Runs inside a Docker container on port 5000.

### MySQL
- Relational database for storing persistent data.
- Stores data for the Flask application.
- Configured via environment variables in Docker.
- Healthchecked so Flask waits until it’s ready.
- Uses a Docker volume for data persistence.

### Redis
- In-memory key-value store used for caching.
- Stores a test key `test_key` for Flask to read.
- Provides fast access to temporary data.
- Configured via environment variable `REDIS_URL`.
- Runs in a separate Docker container on port 6379.

## How to Run

```bash
# Build and start all services
docker-compose up --build -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down



