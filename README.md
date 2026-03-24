# Notification Engine

A production-grade, event-driven backend system for processing and delivering notifications asynchronously across multiple channels.

## Overview

This project implements a scalable notification system using FastAPI, Celery, Redis, and PostgreSQL. It follows a clean architecture approach and demonstrates how to design and build an event-driven backend service capable of handling asynchronous workloads.

The system accepts events, processes them in the background, generates notifications, and delivers them through different channels.

## Features

* Event ingestion via REST API
* Asynchronous processing using Celery
* Redis as message broker and cache
* PostgreSQL for persistent storage
* Multi-channel notification delivery (in-app, email mock, SMS placeholder)
* Scheduling support using Celery ETA/countdown
* Retry mechanism with exponential backoff
* Rate limiting using Redis
* Logging and monitoring support
* Clean architecture with modular design

## Architecture

The system is built using an event-driven architecture:

API Layer (FastAPI)
→ Event Service
→ Celery Task Queue (Redis)
→ Worker Processes (Celery)
→ Notification Service
→ Delivery Layer (Channel Handlers)
→ Database (PostgreSQL)

## Tech Stack

* FastAPI
* Python
* PostgreSQL
* Redis
* Celery
* SQLAlchemy
* Docker and Docker Compose

## Getting Started

### Prerequisites

* Docker
* Docker Compose

### Installation

Clone the repository:

```
git clone <your-repo-url>
cd notification-engine
```

### Run the system

```
docker compose up --build
```

### Access API

```
http://localhost:8000/docs
```

## API Endpoints

### Create Event

POST /events

Request body:

```
{
  "event_type": "user_registered",
  "payload": {
    "user_id": 1,
    "message": "Welcome to the platform"
  }
}
```

## How It Works

1. Client sends an event to the API
2. Event is stored in the database
3. Celery task is triggered asynchronously
4. Worker processes the event
5. Notifications are created
6. Delivery service sends notifications via appropriate channel

## Async Processing

Celery workers handle all background tasks. The API remains fast and non-blocking by delegating heavy processing to workers.

## Rate Limiting

Rate limiting is implemented using Redis to prevent excessive notifications per user.

## Retry Mechanism

Failed notification deliveries are retried automatically using Celery's retry and backoff features.

## Future Improvements

* Real email provider integration (SendGrid, AWS SES)
* Notification templates
* Authentication and authorization (JWT)
* Monitoring dashboard
* Deployment to cloud (AWS/GCP)

## Status

This project is a fully functional prototype designed with production-level architecture and scalability in mind.

## License

MIT License
