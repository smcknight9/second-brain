# Second Brain

Second Brain is a self-hosted, extensible journaling system powered by **FastAPI, PostgreSQL, and Docker**.  
It allows users to write and retrieve journal entries via a **REST API** or **GraphQL API**, with future plans for search, embeddings, and intelligent tagging.

---

## Features
- **FastAPI backend** for efficient API interactions.
- **PostgreSQL database** for structured journal storage.
- **Dockerized architecture** for easy deployment.
- **Alembic for migrations** to manage database schema changes.
- **REST API** for simple CRUD operations.
- **GraphQL API** (planned) for flexible queries 
- **CLI interface** (planned) for quick terminal-based interactions.

---

## Tech Stack
| Component              | Technology |
|------------------------|------------|
| **Backend API**        | FastAPI (Python) |
| **Database**           | PostgreSQL |
| **GraphQL**           | Strawberry-GraphQL |
| **CLI** *(Planned)*   | Typer / Click / argparse |
| **Task Queue** *(Planned)* | Celery / FastAPI `BackgroundTasks` |
| **Containerization**   | Docker & Docker Compose |
| **Authentication** *(Future-proofing)* | OAuth2 / Token-based auth |

---

## Installation

### 1. Prerequisites
- [Docker](https://www.docker.com/)
- [Python 3.11](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### 2. Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/second-brain.git
cd second-brain
docker compose up --build -d
```
