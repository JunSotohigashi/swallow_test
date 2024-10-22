# Swallow_Test
## Description
This is a test project of Llama Swallow LLM.

## Usage
### Build Docker Image
```
./docker/build.sh
```
### Create Container and attach shell as YOU
```
./docker/run.sh
```
This script do these automaticaly:
- mount project directory (./ProjectName) to /workspace
- create new user (the same name, UID, GID) in the container
- attach all GPUs
- login to bash

You need to keep the container run with this script when you attach VSCode to it.

### Create Container and attach shell as root
```
docker run --rm -it \
    --gpus all \
    -v .:/workspace \
    -e TERM=xterm-256color \
    IMAGE_NAME \
    bash
```

### Create Container and exec COMMAND as YOU
```
docker run --rm -it \
    --gpus all \
    -v .:/workspace \
    -e TERM=xterm-256color \
    -u $(id -u):$(id -g)
    IMAGE_NAME \
    COMMAND
```
A new user isn't created in the container, but UID and GID are set as yours.  
Username will be shown as "I have no name!" if you run "bash" with this way.

### Attach VSCode
- Install "Docker" and "Dev Containers" extentions.
- Run ./docker/run.sh and keep a shell open
- VSCode -> Docker -> CONTAINERS -> Individual Containers -> Your Image -> Attach Visual Studio Code

The first time you attach, a default user is root.
You can use a vscode as yourself by modifying config file.

Type "Open Container Configuration file" into command palette.  
```
{
	"remoteUser": "${localEnv:USER}",
	"workspaceFolder": "/workspace"
}
```
