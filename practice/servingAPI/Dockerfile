FROM amd64/python:3.9-slim

RUN apt-get update && apt-get install -y \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN cd /tmp && \
    wget https://dl.min.io/client/mc/release/linux-arm64/mc && \
    chmod +x mc && \
    mv mc /usr/bin/mc

WORKDIR /usr/app

RUN pip install -U pip &&\
    pip install mlflow==1.30.0 pandas scikit-learn "fastapi[all]" psycopg2-binary

CMD ["python", "save_model_to_registry.py", "&&", "uvicorn", "app:app", "--host", "0.0.0.0", "--reload"]
