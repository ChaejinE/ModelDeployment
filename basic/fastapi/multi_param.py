from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False):
    '''
        Path Parameter & Query Parameter를 모두 사용한 Path Operation Function
        q, short : Query Parameters
        user_id, item_id : Path Parameters

        URL 후보
        http://localhost:8000/users/3/items/foo-item?q=hello&short=True
        http://localhost:8000/users/3/items/foo-item?short=True
        http://localhost:8000/users/3/items/foo-item?q=hello
        http://localhost:8000/users/3/items/foo-item

    '''
    item = {"item_id": item_id, "owner_id": user_id}

    if q:
        item.update({'q': q})
    if not short:
        item.update({"description": "This is an amazing item that has a long description"},)
    
    return item