import os
import random
import httpx
import pytest
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

API_HOST = os.getenv("API_HOST", "http://localhost")
API_PORT = os.getenv("API_PORT", "8001")
BASE_URL = f"{API_HOST}:{API_PORT}"

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture
async def async_client():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        yield client

@pytest.mark.anyio
async def test_create_person(async_client):
    
    response = await async_client.post("/persons/", json={
        "PersonType": "EM",
        "NameStyle": False,
        "Title": "Mr.",
        "FirstName": "John",
        "MiddleName": "H.",
        "LastName": "Doe",
        "Suffix": "Jr.",
        "EmailPromotion": 0,
        # "AdditionalContactInfo": "<info>None</info>",
        # "Demographics": "<demo>None</demo>"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["FirstName"] == "John"
    assert data["LastName"] == "Doe"

@pytest.mark.anyio
async def test_read_person(async_client):
    # First create a person to read
    create_response = await async_client.post("/persons/", json={
        "PersonType": "EM",
        "NameStyle": False,
        "Title": "Mr.",
        "FirstName": "Jane",
        "MiddleName": "A.",
        "LastName": "Smith",
        "Suffix": "III",
        "EmailPromotion": 1,
        # "AdditionalContactInfo": "<info>None</info>",
        # "Demographics": "<demo>None</demo>"
    })
    assert create_response.status_code == 200
    person_id = create_response.json()["BusinessEntityID"]

    # Now read the person
    read_response = await async_client.get(f"/persons/{person_id}")
    assert read_response.status_code == 200
    data = read_response.json()
    assert data["FirstName"] == "Jane"
    assert data["LastName"] == "Smith"

@pytest.mark.anyio
async def test_update_person(async_client):
    # First create a person to update
    create_response = await async_client.post("/persons/", json={
        "PersonType": "EM",
        "NameStyle": False,
        "Title": "Mr.",
        "FirstName": "Jim",
        "MiddleName": "B.",
        "LastName": "Beam",
        "Suffix": "",
        "EmailPromotion": 0,
        # "AdditionalContactInfo": "<info>None</info>",
        # "Demographics": "<demo>None</demo>"
    })
    assert create_response.status_code == 200
    person_id = create_response.json()["BusinessEntityID"]

    # Now update the person
    update_response = await async_client.put(f"/persons/{person_id}", json={
        "PersonType": "EM",
        "NameStyle": True,
        "Title": "Dr.",
        "FirstName": "Jim",
        "MiddleName": "B.",
        "LastName": "Beam",
        "Suffix": "Sr.",
        "EmailPromotion": 2,
        # "AdditionalContactInfo": "<info>Updated</info>",
        # "Demographics": "<demo>Updated</demo>"
    })
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["NameStyle"] == True
    assert data["Title"] == "Dr."
    assert data["Suffix"] == "Sr."
    assert data["EmailPromotion"] == 2

@pytest.mark.anyio
async def test_delete_person(async_client):
    # First create a person to delete
    create_response = await async_client.post("/persons/", json={
        "PersonType": "EM",
        "NameStyle": False,
        "Title": "Mr.",
        "FirstName": "Ethan",
        "MiddleName": "M.",
        "LastName": "Hunt",
        "Suffix": "",
        "EmailPromotion": 0,
        # "AdditionalContactInfo": "<info>None</info>",
        # "Demographics": "<demo>None</demo>"
    })
    assert create_response.status_code == 200
    person_id = create_response.json()["BusinessEntityID"]

    # Now delete the person
    delete_response = await async_client.delete(f"/persons/{person_id}")
    assert delete_response.status_code == 200

    # Try to read the deleted person
    read_response = await async_client.get(f"/persons/{person_id}")
    assert read_response.status_code == 404

@pytest.mark.anyio
async def test_health_check(async_client):
    response = await async_client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
