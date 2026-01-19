pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Test Script') {
            steps {
                sh '''
                    chmod +x script/count_files.sh
                    bash -n script/count_files.sh
                    script/count_files.sh
                '''
            }
        }

        stage('Build RPM') {
            agent {
                docker {
                    image 'fedora:latest'
                    args '-u root'
                }
            }
            steps {
                sh '''
                    dnf install -y rpm-build rpmdevtools
                    rpmdev-setuptree

                    mkdir -p ~/rpmbuild/SOURCES/file-counter-1.0
                    cp script/count_files.sh ~/rpmbuild/SOURCES/file-counter-1.0/

                    cd ~/rpmbuild/SOURCES
                    tar czvf file-counter-1.0.tar.gz file-counter-1.0

                    cp ${WORKSPACE}/rpm/file_counter.spec ~/rpmbuild/SPECS/
                    rpmbuild -ba ~/rpmbuild/SPECS/file_counter.spec

                    cp ~/rpmbuild/RPMS/noarch/*.rpm ${WORKSPACE}/rpm/
                '''
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: 'rpm/*.rpm'
            echo 'Pipeline finished successfully'
        }
        failure {
            echo 'Pipeline failed'
        }

stage('Build DEB') {
    agent {
        docker {
            image 'ubuntu:22.04'
            args '-u root'
        }
    }
    steps {
        sh '''
            apt-get update
            apt-get install -y dpkg-dev

            mkdir -p build/file-counter/usr/local/bin
            mkdir -p build/file-counter/DEBIAN

            cp script/count_files.sh build/file-counter/usr/local/bin/file-counter
            chmod 755 build/file-counter/usr/local/bin/file-counter
            cp deb/DEBIAN/control build/file-counter/DEBIAN/control

            dpkg-deb --build build/file-counter
            cp build/file-counter.deb ${WORKSPACE}/
        '''
    }
}


    }
}

