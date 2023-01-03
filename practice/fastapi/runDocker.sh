#!/bin/bash

docker run -d \
  --rm \
  --name api-server \
  -p 8000:8000 \
  my-api-server
