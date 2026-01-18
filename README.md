# File Counter

Bash script that counts regular files in /etc directory

## Script
script/count_files.sh

## RPM
rpm/file_counter.spec
rpm/file_counter-1.0-1.noarch.rpm

##Build RPM
rpmbuild -ba file_counter.spec

## Install RPM
sudo rpm -i --nodeps file_couner-1.0-1.noarch.rpm

## Run
count_files.sh

## Jenkins (Docker)

Jenkins is run using Docker.

Build image:
```bash
docker build -t jenkins-local .
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins jenkins-local
```
Build Jenkins image
docker build -t jenkins-local .

Run Jenkins container
docker run -d \
  -p 8080:8080 \
  -p 50000:50000 \
  --name jenkins \
  jenkins-local


Jenkins web interface is available at:

http://localhost:8080
