pipeline {
    agent any
   environment {
    PATH = "C:/Users/Admin/AppData/Local/Programs/Python/Python312;$PATH"
}

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                checkout([$class: 'GitSCM', branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/Anusri-Rao676/webhook-jenkins.git']]])
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Pytest') {
            steps {
                echo 'Running Pytest tests...'
                sh 'pytest --verbose'
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pytest tests passed successfully!'
        }
        failure {
            echo 'Pytest tests failed. Check console output for details.'
        }
    }
}
