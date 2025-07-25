pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Version') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Hello') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Checkout') {
            steps {
                echo '📦 Checking out repository...'
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/Anusri-Rao676/webhook-jenkins.git']]])
            }
        }

        stage('Setup') {
            steps {
                echo '🐍 Confirming Python setup...'
                sh 'python3 --version'
                sh 'echo $PATH'
                sh 'which python3'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Creating virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run App') {
            steps {
                echo '🚀 Running Python app...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python app.py
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Executing tests...'
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest --verbose
                '''
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline complete.'
        }
        success {
            echo '🎉 Tests passed successfully!'
        }
        failure {
            echo '❌ Tests failed. Check logs for details.'
        }
    }
}
