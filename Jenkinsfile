pipeline {
    agent any

    environment {
        PATH = "/usr/bin:${env.PATH}"
    }

    stages {
        stage('Custom PATH') {
            steps {
                echo '🔍 PATH configuration check...'
                sh 'echo $PATH'
                sh 'which python3'
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

        stage('Run Python Script') {
            steps {
                echo '🐍 Running local Python script...'
                sh 'python3 --version'
                sh 'python3 app.py'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing Python dependencies...'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                echo '🧪 Running Pytest tests...'
                sh 'pytest --verbose'
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline finished.'
        }
        success {
            echo '🎉 Pytest tests passed successfully!'
        }
        failure {
            echo '❌ Pytest tests failed. Check console output for details.'
        }
    }
}
