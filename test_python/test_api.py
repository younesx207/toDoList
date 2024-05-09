from fastapi.testclient import TestClient

import os
import sys


sys.path.append(os.getcwd())
sys.path.append('./app')
from main import app

client = TestClient(app)

def test_docs():
    res= client.get("/docs")
    assert res.status_code == 200


# Ecrire test /redocs
    
def test_redoc():
    res = client.get("/redoc")
    assert res.status_code == 200