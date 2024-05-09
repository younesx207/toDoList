
from pydantic import BaseModel


# DTO : Data Transfert Object ou Schema
# Représente la structure de la données (data type) en entrée ou en sortie de notre API.
# Model Pydantic = Datatype

class TodoNoID(BaseModel):
    name: str
    

class Todo(BaseModel):
    id: str
    name: str
    
    
class User(BaseModel):

    email: str
    password: str
    

class UserLogin(BaseModel):

    email: str
    password: str
    
# define how we except the request body to be
class Config:
    schema_extra={
        "exemple": {
            "email": "benalioune6@gmail.com",
            "password": "abcdef"
        }
    }
    

    
    
users = [
    
    User(email="benalioune6@gmail.com", password="pass")
    
]
    

Todos = [
    Todo(id="efe", name="Adama"),
    Todo(id="fef", name="Adrien"),
    Todo(id="dfd", name="Akbar"),
    Todo(id="frf", name="Alioune")
]



