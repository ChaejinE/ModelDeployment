"""
Reference : https://mlops-for-mle.github.io/tutorial/docs/fastapi/fastapi-tutorial
FastAPI MLOps Basic
"""
from fastapi import FastAPI

# uvicorn main:app --reload 에서
# main : main.py
# app : FastAPI() 객체. 변수명이 달라지면 uvicorn 명령어에서 app이 달라진다.
app = FastAPI()


@app.get("/")  # : Path Operation(GET,POST,PUT,DELETE) 이라 부른다.
def read_root():  # : Path Operation을 호출하는 함수로, Path Operation Function이라 부른다.
    return {"Hello": "World"}  # : dict, list, str, int 등을 Return 할 수 있다.
