pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Script') {
            steps {
                sh '''
                    chmod +x count_files.sh
                    bash -n count_files.sh
                    ./count_files.sh
                '''
            }
        }
    }
}

