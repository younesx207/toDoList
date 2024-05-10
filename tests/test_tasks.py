
import pytest
from fastapi.testclient import TestClient
from main import app
import httpx
from fastapi.testclient import TestClient
from firebase_admin import auth
from database.firebase import authTodo


client = TestClient(app)


# Test pour faire un get all sur les tâches
def test_get_all_tasks(cleanup):
    client.post("/auth/signup", json={"email": "test_younes@example.com", "password": "testpassword"})
    
    auth_token = authTodo.sign_in_with_email_and_password(email="test_younes@example.com", password="testpassword")['idToken']
    auth_headers= {"Authorization": f"Bearer {auth_token}"}

    response = client.get("/todos/todos", headers=auth_headers)
    assert response.status_code == 200

def test_get_all_tasks_unauthorized(cleanup):
    # On n'effectue aucune inscription ni authentification
    
    response = client.get("/todos/todos")
    
    # On vérifie que le code de status est 401 (non autorisé)
    assert response.status_code == 401

#Test pour ajout
def test_add_new_task(cleanup):
    client.post("/auth/signup", json={"email": "younes@gmail.com", "password": "younes"})
    
    # Création des données de la tâche
    auth_token = authTodo.sign_in_with_email_and_password(email="younes@gmail.com", password="younes")['idToken']
    auth_headers = {"Authorization": f"Bearer {auth_token}"}
    
    task_data = {
        "id": "1223",
        "name": "Test"
    }
    response = client.post("/todos/todos", headers=auth_headers, json=task_data)
    assert response.status_code == 201
    # Vérifier que la tâche a été créée
    new_task = response.json()
    assert new_task["name"] == task_data["name"]

    # # Suppression
    # task_id = response.json()["id"]
    # print(task_id)

    # # Supprimer la tâche après
    # response = client.delete(f"/todos/{task_id}", headers=auth_headers)
    # assert response.status_code == 202



def test_get_task_by_id(cleanup):
    # Créer un utilisateur de test
    client.post("/auth/signup", json={"email": "test_user@example.com", "password": "testpassword"})
    auth_token = authTodo.sign_in_with_email_and_password(email="test_user@example.com", password="testpassword")['idToken']
    auth_headers = {"Authorization": f"Bearer {auth_token}"}
      
    # Créer une nouvelle tâche pour le test
    task_data = {
        "id": "122",
        "name": "Test2"
    }

    # Envoyer la requête POST avec le paramètre json
    response = client.post("/todos/todos", headers=auth_headers, json=task_data)
    assert response.status_code == 201
    task_id = response.json()["id"]
    print(task_id)
    # Appelez la fonction get_task_by_id pour obtenir les détails de la tâche
    response = client.get(f"/todos/todos/{task_id}", headers=auth_headers)
    # Requête réussie (code de statut 204)
    assert response.status_code == 200
    # # Supprimer la tâche après
    # response = client.delete(f"/todos/todos/{task_id}", headers=auth_headers)
    # assert response.status_code == 202

def test_delete_task_by_id(cleanup):
    # Créer un utilisateur de test
    client.post("/auth/signup", json={"email": "test_user@example.com", "password": "testpassword"})
    auth_token = authTodo.sign_in_with_email_and_password(email="test_user@example.com", password="testpassword")['idToken']
    auth_headers = {"Authorization": f"Bearer {auth_token}"}

    # Créer une nouvelle tâche pour le test
    task_data = {
        "id": "54213420-1a64-4dc3-a9b4-50d5aa584bck",
        "name": "Test"
    }
    response = client.post("/todos/todos", headers=auth_headers, json=task_data)
    assert response.status_code == 201
    task_id = response.json()["id"]

    # Supprimer la tâche avec le task_id
    response = client.delete(f"/todos/{task_id}", headers=auth_headers)

    # Suppression avec succès (code de statut 200)
    assert response.status_code == 202
    # assert response.json() == {"message": "Task deleted"}



def test_patch_task_by_id(cleanup):
    # Créer un utilisateur de test
    client.post("/auth/signup", json={"email": "test_user@example.com", "password": "testpassword"})
    auth_token = authTodo.sign_in_with_email_and_password(email="test_user@example.com", password="testpassword")['idToken']
    auth_headers = {"Authorization": f"Bearer {auth_token}"}

    # Créer une nouvelle tâche pour le test
    task_data = {
        "id": "54213420-1a64-4dc3-a9b4-50d5aa584bca",
        "name": "Test"
    }
    response = client.post("/todos/todos", headers=auth_headers, json=task_data)
    assert response.status_code == 201
    task_id = response.json()["id"]

    # Mettre à jour partiellement la tâche avec le task_id
    updated_task_data = {
        "name": "Test7",
    }
    response = client.patch(f"/todos/{task_id}", headers=auth_headers, json=updated_task_data)

    # Vérifier si la tâche a été mise à jour avec succès (code de statut 200)
    assert response.status_code == 204
    # # Vérifier si les données de la tâche ont été mises à jour correctement
    # updated_task = response.json()
    # assert updated_task["name"] == updated_task_data["name"]
    # # Supprimer la tâche après
    # response = client.delete(f"/todos/todos/{task_id}", headers=auth_headers)
    # assert response.status_code == 202