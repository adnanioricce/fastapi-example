# FastAPI CRUD API with PostgreSQL

this is a learning project to explore the fastapi framework

## Features

- Create a new person
- Read person details
- Update person information
- Delete a person
- Health check endpoint

## Project Structure

- `app/`: Contains the FastAPI application, including models, schemas, CRUD operations, and API routes.
- `tests/`: Contains end-to-end (E2E) tests for the API.
- `.env`: Environment variables for configuration.
- `Dockerfile`: Docker configuration for containerizing the FastAPI app.
- `docker-compose.yml`: Docker Compose configuration for setting up the FastAPI app and PostgreSQL database.

## Requirements

- Python 3.8+
- Docker and Docker Compose
- PostgreSQL

## Getting Started

### Setup Environment Variables

Create a `.env` file in the project root with the following content:

```shell
API_HOST=http://localhost
API_PORT=8000
SQLALCHEMY_DATABASE_URL=postgresql://username:password@db:5432/person_db
```

Replace username and password with your PostgreSQL credentials.

### Build and Run with Docker

Build the Docker images and start the containers:

```bash
docker-compose up --build
```
The API will be accessible at http://localhost:8000.

### Run the Tests

To run the E2E tests:

Ensure the API and PostgreSQL are running in Docker containers as described above.

Install the required Python packages for testing:

```bash
pip install pytest httpx pytest-asyncio
```

### Run the tests using pytest:

```bash
pytest tests/test_e2e.py
```
## API Endpoints

POST /persons/: Create a new person
GET /persons/{person_id}: Read person details
PUT /persons/{person_id}: Update person information
DELETE /persons/{person_id}: Delete a person
GET /health: Health check endpoint

### Example Requests

#### Create a Person

```bash

curl -X POST "http://localhost:8000/persons/" -H "Content-Type: application/json" -d '{
  "BusinessEntityID": 1,
  "PersonType": "EM",
  "NameStyle": false,
  "Title": "Mr.",
  "FirstName": "John",
  "MiddleName": "H.",
  "LastName": "Doe",
  "Suffix": "Jr.",
  "EmailPromotion": 0,
  "AdditionalContactInfo": "<info>None</info>",
  "Demographics": "<demo>None</demo>"
}'
```
#### Read a Person

```bash

curl -X GET "http://localhost:8000/persons/1"
```

#### Update a Person

```bash

curl -X PUT "http://localhost:8000/persons/1" -H "Content-Type: application/json" -d '{
  "PersonType": "EM",
  "NameStyle": true,
  "Title": "Dr.",
  "FirstName": "John",
  "MiddleName": "H.",
  "LastName": "Doe",
  "Suffix": "Sr.",
  "EmailPromotion": 1,
  "AdditionalContactInfo": "<info>Updated</info>",
  "Demographics": "<demo>Updated</demo>"
}'
```

#### Delete a Person

```bash

curl -X DELETE "http://localhost:8000/persons/1"
```

#### Health Check

```bash
curl -X GET "http://localhost:8000/health"
```