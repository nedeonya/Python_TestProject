from typing import List
from fastapi import FastAPI, HTTPException, Depends
from api.repository import UserRepository, User

app = FastAPI()


@app.get("/users/{user_id}", status_code=200)
def get_user(user_id: int, user_repo: UserRepository = Depends()):
    user_by_id = user_repo.get_user_by_id(user_id)
    if user_by_id is not None:
        return user_by_id
    else:
        raise HTTPException(status_code=404, detail=f"User with id = '{user_id}' does not exist")


@app.post("/users", status_code=201)
def create_user(user: User, user_repo: UserRepository = Depends()):
    user_repo.create_user(user)
    return user


@app.put("/users/{user_id}", status_code=201)
def update_user(user: User, user_repo: UserRepository = Depends()):
    updated_user = user_repo.update_user(user)
    if updated_user is not None:
        return updated_user
    else:
        raise HTTPException(status_code=404, detail=f"User with id = '{user.id}' does not exist")


@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int, user_repo: UserRepository = Depends()):
    user_to_delete = user_repo.delete_user(user_id)
    if user_to_delete is None:
        raise HTTPException(status_code=404, detail=f"User with id = '{user_id}' does not exist")