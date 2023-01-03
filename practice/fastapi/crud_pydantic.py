"""
Request Body : Client에서 API로 전송하는 Data
Response Body : API가 Client로 전송하는 데이터
Pydantic Model을 통해 Client, API 사이 데이터를 주고 받는 데이터 형식을 지정해준다.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define Input Schema
class CreateIn(BaseModel):
    """
    Request Body의 구성 요소가 될 변수들(name, nickname)을 attribute로 지정
    """

    name: str
    nickname: str


# Define Output Schema
class CreateOut(BaseModel):
    """
    Response Body의 구성 요소가 될 변수들을 attribute로 지정
    """

    status: str
    id: int


app = FastAPI()

USER_DB = {}

NAME_NOT_FOUND = HTTPException(status_code=400, detail="Name not found")

# Create
@app.post("/users", response_model=CreateOut)
def create_user(user: CreateIn) -> CreateOut:
    USER_DB[user.name] = user.nickname
    return CreateOut(status="success", id=len(USER_DB))
