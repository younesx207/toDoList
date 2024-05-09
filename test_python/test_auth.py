
from fastapi.testclient import TestClient
from main import app  # Assurez-vous d'ajuster le chemin si nécessaire
from unittest.mock import patch

# Mock de la fonction auth.create_user pour éviter d'appeler Firebase lors des tests
@patch("firebase_admin.auth.create_user")
def test_signup(mock_create_user):
    client = TestClient(app)

    # Données utilisateur fictives pour le test
    user_data = {"email": "test@example.com", "password": "password"}

    # Simuler la création d'utilisateur dans Firebase
    mock_create_user.return_value.uid = "mocked_uid"

    # Exécuter la requête de test
    response = client.post("/auth/signup", json=user_data)

    assert response.status_code == 200

    # Assurez-vous que la fonction create_user a été appelée avec les bonnes données
    mock_create_user.assert_called_once_with(email=user_data["email"], password=user_data["password"])

    print(f"User data: {user_data}")
    print(f"Mock create_user arguments: {mock_create_user.call_args}")

# Mock de la fonction authStudent.sign_in_with_email_and_password pour éviter d'appeler Firebase lors des tests
@patch("database.firebase.authTodo.sign_in_with_email_and_password")
def test_login(mock_sign_in):
    client = TestClient(app)

    # Données de connexion fictives pour le test
    login_data = {"username": "test@example.com", "password": "testpassword"}

    # Simuler la connexion avec Firebase
    mock_sign_in.return_value = {"idToken": "mocked_token"}

    # Exécuter la requête de test
    response = client.post("/auth/login", data=login_data)

    assert response.status_code == 200
    assert response.json() == {"access_token": "mocked_token", "token_type": "bearer"}

    # Assurez-vous que la fonction sign_in_with_email_and_password a été appelée avec les bonnes données
    mock_sign_in.assert_called_once_with(email="test@example.com", password="testpassword")