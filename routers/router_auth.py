from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import os
import sys


# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.getcwd()))

from database.firebase import db


from fastapi.security import OAuth2PasswordBearer

from classes.schemas_dto import User
from firebase_admin import auth
from database.firebase import authTodo


import uuid

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')
def get_current_user(provided_token: str = Depends(oauth2_scheme)):
    decoded_token = auth.verify_id_token(provided_token)
    decoded_token['idToken'] = provided_token
    return decoded_token

router  =  APIRouter(
    
    tags=["Auth"],
    prefix='/auth'
    
)
#signup endPoint
@router.post('/signup', status_code=201)
async def signup(user_data:User):
    email = user_data.email
    password = user_data.password
    
    try:
        
        user = auth.create_user(
            email = email,
            password = password
        )
        newUser = User(email=email, password=password)
        
        generatedId=uuid.uuid4()
        
        db.child("user").child(generatedId).set(newUser.model_dump())
        
        
        return JSONResponse(content={
            "message" :  f"User account created successfully for user {user.uid}"
        })
        
    except auth.EmailAlreadyExistsError: 
        raise HTTPException(
            status_code=401,
            detail= f"account already created for the user {user.email}"
        )
    

   

#login endPoint

@router.post('/login')
async def create_swagger_token(user_credentials: OAuth2PasswordRequestForm = Depends()):
    try :
        user = authTodo.sign_in_with_email_and_password(email=user_credentials.username, password=user_credentials.password)
        token = user['idToken']
        print(token)
        return {
            'access_token': token,
            'token_type': 'bearer'
        }
    except :
        raise HTTPException(status_code=401, detail='Invalid credentials')

               

 
#protect route to get personal data 
@router.get('/me')
def secure_endpoint(user_data: int = Depends(get_current_user)):
    return user_data
