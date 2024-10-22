#!/bin/bash

IMAGE_NAME='junsotohigashi/swallow_test:latest'

docker run --rm -it \
    --gpus all \
    -v .:/workspace \
    -e HOST_UID=$(id -u) \
    -e HOST_GID=$(id -g) \
    -e HOST_UNAME=$(id -un) \
    -e HOST_GNAME=$(id -gn) \
    -e TERM=xterm-256color \
    $IMAGE_NAME \
    bash
