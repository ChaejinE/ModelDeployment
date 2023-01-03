from fastapi import FastAPI, HTTPException

app = FastAPI()

USER_DB = {}

NAME_NOT_FOUND = HTTPException(status_code=400, detail="Name not found.")

# Create
@app.post("/user/name/{name}/nickname/{nickname}")
def create_user(name: str, nickname: str):
    """
    이름, 별명을 USER_DB에 저장
    """
    USER_DB[name] = nickname
    return {"status": "success"}


# Read
@app.get("/users/name/{name}")
def read_user(name: str):
    """
    USER_DB에서 별명을 찾아 return
    """
    if name not in USER_DB:
        raise NAME_NOT_FOUND

    return {"nickname": USER_DB[name]}


# Update
@app.put("/users/name/{name}/nickname/{nickname}")
def update_user(name: str, nickname: str):
    """
    USER_DB에서 새로운 별명으로 데이터를 갱신
    """
    if name not in USER_DB:
        raise NAME_NOT_FOUND

    USER_DB[name] = nickname
    return {"status": "success"}


# Delete
@app.delete("/users/name/{name}")
def delete_user(name: str):
    """
    USER_DB에서 해당 이름을 보유한 데이터 삭제
    """
    if name not in USER_DB:
        raise NAME_NOT_FOUND

    del USER_DB[name]
    return {"status": "success"}
