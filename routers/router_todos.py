from fastapi import APIRouter, Depends, HTTPException
from classes.schemas_dto import Todos
from classes.schemas_dto import Todo
from classes.schemas_dto  import TodoNoID
from typing import List
from routers.router_auth import get_current_user
from uuid import uuid4


from database.firebase import db



import uuid



router = APIRouter(
    prefix='/todos',
    tags=['Todos']
)


# Verbs + Endpoints
@router.get("/todos", response_model=List[Todo])
async def get_todo(user_data: int= Depends(get_current_user)):
    queryResults = db.child("todo").get(user_data['idToken']).val()
    if not queryResults : return []
    todoArray = [Todo(**value) for value in queryResults.values()]
    return todoArray 




# 1. Exercice (10min) Create new Todo: POST
# response_model permet de définir de type de réponse (ici nous retournons le todo avec sont id)
# status_code est définit sur 201-Created car c'est un POST
@router.post("/todos", status_code=201, response_model=Todo)
async def create_todo(todo: Todo, user_data: int= Depends(get_current_user)):
    generatedId=str(uuid4())
    newTodo = Todo (id=generatedId, name=todo.name)
    db.child('todo').child(generatedId).set(data=newTodo.model_dump(), token=user_data['idToken'])
    return newTodo


# 2. Exercice (10min) Todo GET by ID
# response_model est un Todo car nous souhaitons trouvé l'étudiant correspodant à l'ID
@router.get('/todos/{todo_id}', response_model=Todo)
async def get_todo_by_id(todo_id: str, user_data: int= Depends(get_current_user)):
    queryResult = db.child('todo').child(todo_id).get(user_data['idToken']).val()
    if not queryResult : raise HTTPException(status_code=404, detail="Todo not found") 
    return queryResult




# 3. Exercice (10min) PATCH Todo (name)
@router.patch('/{todo_id}', status_code=204)
async def todo_update(todo_id: str, todo: TodoNoID, user_data: int= Depends(get_current_user)):
    queryResult = db.child('todo').child(todo_id).get(user_data['idToken']).val()
    if not queryResult : raise HTTPException(status_code=404, detail="Todo not found") 
    updatedTodo = Todo(id=todo_id, **todo.model_dump())
    db.child('todo').child(todo_id).update(data=updatedTodo.model_dump(), token=user_data['idToken'])
    return "toDo updated succssefully"


# # 4. Exercice (10min) DELETE Todo
# @router.delete("/{t_id}", status_code=202, response_model=str)
# async def todo_delete(todo_id: str, user_data: int= Depends(get_current_user)) :
#     queryResult = db.child('todo').child(todo_id).get(user_data['idToken']).val()
#     if not queryResult : 
#         raise HTTPException(status_code=404, detail="Todo not found")
#     db.child('todo').child(todo_id).remove(token=user_data['idToken'])
#     return "Todo deleted"

# @router.delete('/{todo_id}', status_code=202)
# async def delete_todo_by_id(todo_id: str, userData: int = Depends(get_current_user)):
#     task_data = db.child("todo").child(todo_id).get(userData['idToken']).val()
#     if task_data:
#         # Supprimez la tâche de la base de données Firebase
#         db.child("todo").child(todo_id).remove()
#         return {"message": "Task deleted"}
#     else:
#         raise HTTPException(status_code=404, detail="Task not found")


#DELETE Request
@router.delete("/{todo_id}", status_code=202, response_model=str)
async def todo_delete(todo_id: str, user_data: int= Depends(get_current_user)) :
    queryResult = db.child('todo').child(todo_id).get(user_data['idToken']).val()
    if not queryResult : 
        raise HTTPException(status_code=404, detail="Event not found")
    db.child('todo').child(todo_id).remove(token=user_data['idToken'])
    return "todo deleted"

