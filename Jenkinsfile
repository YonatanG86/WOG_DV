pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YonatanG86/WOG_DV.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Test') {
            steps {
                sh 'python e2e.py || true'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose push'
            }
        }
    }
}