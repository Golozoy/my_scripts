#! /usr/bin/env bash

echo "Run script"
docker stop $(docker ps -aq) &> /dev/null
docker rm $(docker ps -aq) &> /dev/null
docker image rm $(docker images -q) &> /dev/null
docker volume rm $(docker volume ls -q) &> /dev/null
docker network rm $(docker network ls -q) &> /dev/null
echo "Done!"
