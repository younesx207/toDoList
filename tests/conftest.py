from firebase_admin import auth
from main import app
from fastapi.testclient import TestClient
import pytest
import os
from database.firebase import db
from classes.schemas_dto import Todo

os.environ['TESTING'] = 'True'
client = TestClient(app)

@pytest.fixture()
def create_user():
  client.post("/auth/signup", json= {
    "email": "younes@gmail.com",
    "password": "younes"
  })

@pytest.fixture
def auth_user(create_user):
  user_credentials = client.post("auth/login", data={
    "username": "younes@gmail.com",
    "password": "younes"
  })
  return user_credentials.json()

def remove_test_users():
  users = auth.list_users().iterate_all()
  for user in users:
    if user.email.startswith("test."):
      auth.delete_user(user.uid)
    

# @pytest.mark.parametrize("route,method,body", [
#   ("/categories","POST", CategoryNoID(name="Test Category ", description="Test Description").model_dump())
# ])



@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
  request.addfinalizer(remove_test_users)