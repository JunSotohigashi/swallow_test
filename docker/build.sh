#!/bin/bash

IMAGE_NAME='junsotohigashi/swallow_test:latest'

docker build ./docker -t $IMAGE_NAME
docker image prune -f
