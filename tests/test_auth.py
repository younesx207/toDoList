from fastapi.testclient import TestClient
from main import app
import pytest
client = TestClient(app)

def test_valid_user():
  response = client.post("/auth/signup", json= {
    "email": "test.user1@gmail.com",
    "password": "younes"
  })
  assert response.status_code == 201

def test_invalid_user(create_user):
  response = client.post("/auth/signup", json= {
    "email": "younes@gmail.com",
    "password": "younes"
  })
  assert response.status_code == 409