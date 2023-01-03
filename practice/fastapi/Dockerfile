FROM amd64/python:3.8.12-slim

RUN mkdir /usr/app
COPY ./requirements.txt .
COPY ./crud_pydantic.py /usr/app/

RUN pip install -U pip \
    && pip install -r requirements.txt

WORKDIR /usr/app

CMD ["uvicorn", "crud_pydantic:app", "--host", "0.0.0.0", "--reload"]
