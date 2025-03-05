# Second Brain

Second Brain is a self-hosted, extensible journaling system powered by **FastAPI, PostgreSQL, and Docker**.  
It allows users to write and retrieve journal entries via a **REST API**, with future plans for search, embeddings, and intelligent tagging.

---

## Features
- **FastAPI backend** for efficient API interactions.
- **PostgreSQL database** for structured journal storage.
- **Dockerized architecture** for easy deployment.
- **Alembic for migrations** to manage database schema changes.
- **REST API** for simple CRUD operations.
- **CLI interface** for quick terminal-based interactions.

---

## Tech Stack
| Component              | Technology |
|------------------------|------------|
| **Backend API**        | FastAPI (Python) |
| **Database**           | PostgreSQL |
| **CLI**               | Typer |
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
git clone https://github.com/smcknight9/second-brain.git
cd second-brain
docker compose up --build -d
```

---

## Usage

### Start the API
To restart or rebuild the API, run:
```sh
docker compose down && docker compose up --build -d
```

### Access the API Container
To open a bash shell in the running API container:
```sh
docker exec -it secondbrain_api bash
```

### CLI Usage
#### Add a Journal Entry
```sh
python cli/cli.py add-entry "This is a CLI journal entry!"
```

#### Retrieve Journal Entries
```sh
python cli/cli.py get-entries
```

This will return a list of journal entries stored in the database.

---

## Roadmap
- [ ] Implement GraphQL API with Strawberry
- [ ] Add authentication (OAuth2 or JWT)
- [ ] Introduce search and embeddings
- [ ] Build a web interface for easy access

---

## License
This project is licensed under the MIT License.

