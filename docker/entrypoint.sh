#!/bin/bash

if [ -z $HOST_UID ] && [ -z $HOST_UNAME ] && [ -z $HOST_GID ] && [ -z $HOST_GNAME ]; then
  bash
else
  groupadd --gid $HOST_GID $HOST_GNAME
  useradd --uid $HOST_UID -g $HOST_GID -m -s /bin/bash $HOST_UNAME
  export HOME=/home/$HOST_UNAME
  exec setpriv --reuid=$HOST_UID --regid=$HOST_GID --init-groups "$@"
fi
