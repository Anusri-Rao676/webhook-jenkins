pipeline {
    agent any

    tools {
        python 'Python 3.9'  // This matches the name you set above
    }

    stages {
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
                echo '📦 Installing dependencies...'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                echo '🚀 Running Python app...'
                sh 'python3 app.py'
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Executing tests...'
                sh 'pytest --verbose'
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
