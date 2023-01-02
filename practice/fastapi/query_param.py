from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/{item_id}")
def read_item(item_id: str, needy: str, skip: int = 0, limit: int = 10):
    '''
        skip, limit은 Path Operation(@app.get("/items")에 들어가있는 변수가 아니다.
        위와 같이 function parameter로 사용되지만, Path Operation에 포함되지 않는 변수를
        : Query Parameter라 한다.
        http://loaclhost:8000/items/?skip=0&limit=10 형태로 사용할 수 있다.
        URL에서 ?뒤에 key=value 형태이고, &로 구분하는 것이 특징이다.
        
        Query Parameter는 고정된 부분이 아니므로 Optional 또는 Default 값을 가질 수 있다.
    '''

    # return fake_items_db[skip : skip + limit]

    # needy의 경우 Query Parameter이며, 기본값을 설정하지 않았으므로 Required Query Parameter 이다.
    # needy라는 Query Parameter를 URL에 포함시켜주지 않으면(?형태로 입력), Error가 발생하며 fucntion에 제대로 동작하지 않는다.
    item = {"item_id": item_id, "needy": needy}
    return item
