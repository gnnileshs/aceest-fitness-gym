pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/gnnileshs/aceest-fitness-gym.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Syntax Check') {
            steps {
                sh 'python -m py_compile app.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t aceest-fitness-gym .'
            }
        }
    }
}