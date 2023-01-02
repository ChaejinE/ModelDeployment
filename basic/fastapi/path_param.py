from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")  # Path에 parameter를 입력할 수 있는데, 이를 Path Parameter라 한다.
def read_item(item_id: int):  # 위의 Path Parameter의 값은 function의 argument로 전달되어 호출된다.
    # 또한 Type Hint는 해당 자료형을 지키지 않을 경우에 대한 HTTP Error에 유용하게 쓰인다.
    return {"item_id": item_id}
