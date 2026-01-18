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
