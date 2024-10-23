FROM python:3.12.7-slim-bookworm

RUN apt update && \
    apt install -y git && \
    apt clean

RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN python3 -m pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
RUN python3 -m pip install --no-cache-dir pytest
RUN python3 -m pip install --no-cache-dir transformers datasets evaluate accelerate

WORKDIR /workspace
RUN chmod 777 /workspace

COPY entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]