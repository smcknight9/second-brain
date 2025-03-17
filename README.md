# Second Brain

Second Brain is a self-hosted, extensible journaling system powered by **FastAPI, PostgreSQL, Docker, and Weaviate**.  
It allows users to write and retrieve journal entries via a **REST API**, with built-in semantic search using vector embeddings and intelligent tagging capabilities.

---

## Features
- **FastAPI backend** for efficient API interactions.
- **PostgreSQL database** for structured journal storage.
- **Dockerized architecture** for easy deployment.
- **Alembic for migrations** to manage database schema changes.
- **REST API** for CRUD operations.
- **CLI interface** for quick terminal-based interactions.
- **Semantic Search** powered by Weaviate.
- **Background indexing tasks** using FastAPI `BackgroundTasks`.
- **Single-entry endpoint** to retrieve a journal entry by UUID.

---

## Tech Stack
| Component              | Technology                        |
|------------------------|-----------------------------------|
| **Backend API**        | FastAPI (Python)                  |
| **Database**           | PostgreSQL                        |
| **CLI**                | Typer                             |
| **Task Queue**         | FastAPI `BackgroundTasks`         |
| **Search & Embeddings**| Weaviate (vector database)        |
| **Containerization**   | Docker & Docker Compose           |
| **Authentication** *(Future)* | OAuth2 / JWT              |

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

### Starting the API
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
Your CLI uses the following commands:

#### Add a Journal Entry
```sh
python cli/cli.py add-entry "Journal Title" "Journal content goes here."
```
*This sends a POST request to create a new journal entry.*

#### Retrieve All Journal Entries
```sh
python cli/cli.py get-entries
```
*This fetches and displays all journal entries stored in the database.*

#### Semantic Search
```sh
python cli/cli.py search "travel"
```
*This command sends a semantic search query to Weaviate to find the best matching journal entry and then retrieves its full details using the single-entry endpoint.*

---

## API Examples

### Add a Journal Entry
```sh
curl -X POST "http://localhost:8000/add_entry/" \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Entry", "content": "This is a test journal entry."}'
```

### Retrieve All Entries
```sh
curl "http://localhost:8000/entries/"
```

### Retrieve a Specific Entry by UUID
```sh
curl "http://localhost:8000/entries/<entry_id>/"
```

### Semantic Search via Weaviate
```sh
curl -X POST "http://localhost:8080/v1/graphql" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ Get { JournalEntry(nearText: { concepts: [\"test\"] }, limit: 1) { _additional { id certainty } } } }"}'
```

*Note: When running from your host, ensure your environment variables (or .env file) override internal container names with `localhost` and the proper mapped ports.*

---

## Re-indexing Data

If you lose your Weaviate embeddings (for example, after a full teardown), you can re-index your journal entries using the provided script:

```sh
python reindex_entries.py
```

*Ensure that your Weaviate volume is preserved (do not use `docker compose down -v` unless you intend to remove the data).*

---

## Docker Compose Configuration

Your `docker-compose.yml` sets up persistent volumes for PostgreSQL and Weaviate. For example, Weaviate is configured as:

```yaml
weaviate:
  image: semitechnologies/weaviate:latest
  container_name: weaviate
  ports:
    - "8080:8080"
  env_file: .env
  volumes:
    - weaviate_data:/var/lib/weaviate
  healthcheck:
    test: ["CMD-SHELL", "curl -f http://localhost:8080/v1/.well-known/ready || exit 1"]
    interval: 5s
    timeout: 5s
    retries: 5
```

*This ensures that Weaviate’s data persists across container restarts unless the volume is explicitly removed.*

---

## Roadmap
- [ ] Implement GraphQL API with Strawberry
- [ ] Add authentication (OAuth2 or JWT)
- [ ] Expand intelligent tagging and categorization
- [ ] Build a user-friendly web interface for easy access
- [ ] Enhance CLI with additional features and improved UX

---

## License
This project is licensed under the MIT License.
