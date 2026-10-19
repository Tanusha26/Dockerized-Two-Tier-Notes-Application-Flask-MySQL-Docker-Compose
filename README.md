# Dockerized-Two-Tier-Notes-Application-Flask-MySQL-Docker-Compose
A two-tier web application built using Flask and MySQL, containerized with Docker and managed using Docker Compose. It enables users to add and view notes with persistent database storage, demonstrating container networking and database connectivity.
# Dockerized Two-Tier Notes Application

A simple web application built using **Flask, MySQL, Docker, and Docker Compose**. It allows users to add and view notes while demonstrating containerization, database connectivity, and persistent storage.

## Tech Stack
- **Frontend:** HTML, CSS
- **Backend:** Python, Flask
- **Database:** MySQL 8.4
- **Containerization:** Docker
- **Orchestration:** Docker Compose

## Features
- Add and view notes through a web interface.
- Store notes in a MySQL database.
- Run Flask and MySQL in separate containers.
- Enable persistent database storage using Docker volumes.
- Connect services through Docker Compose networking.

## Getting Started

**1. Start the application**
```bash
docker compose up --build -d
```

**2. Check container status**
```bash
docker compose ps
```

**3. Open in your browser**

http://localhost:5000

**4. Stop the application**
```bash
docker compose down
```

## Architecture

User → Flask Web Application → MySQL Database

Both services run in separate Docker containers and communicate through Docker's internal network.

## Author
Tanusha Algeti

