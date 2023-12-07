import json
import os

from pydantic import BaseModel
from typing import Optional, List


class User(BaseModel):
    id: Optional[int] = None
    name: str


class UserRepository:

    def read_users(self) -> List[User]:
        file_path = os.path.join(os.path.dirname(__file__), "users.json")
        with open(file_path, "r") as file:
            users = json.load(file)
            user_list = [u for u in users]
        return user_list

    def create_user(self, user: User) -> User:
        users = self.read_users()
        user_id = max([u['id'] for u in users], default=0) + 1
        users.append(user)
        self._write_users(users)
        return user

    def update_user(self, user: User) -> Optional[User]:
        users: list[User] = self.read_users()
        user_by_id = self.get_user_by_id(user.id)
        if user_by_id is not None:
            users.remove(user_by_id)
            users.append(user)
            self._write_users(users)
            return user
        else:
            return None

    def delete_user(self, user_id: int) -> Optional[User]:
        users: list[User] = self.read_users()
        user_by_id = self.get_user_by_id(user_id)
        if user_by_id is not None:
            users.remove(user_by_id)
            file_path = os.path.join(os.path.dirname(__file__), "users.json")
            with open(file_path, "w") as file:
                json.dump(users, file)
        return user_by_id

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        users: list[User] = self.read_users()
        user_by_id = next((u for u in users
                           if u['id'] == user_id), None)
        return user_by_id

    def _write_users(self, users: List[User]):
        file_path = os.path.join(os.path.dirname(__file__), "users.json")
        with open(file_path, "w") as file:
            json.dump(users, file, default=lambda user: user.__dict__)
