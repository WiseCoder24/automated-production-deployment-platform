
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Inspect Workspace') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'git log -1 --oneline'
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/pip install -r application/requirements.txt pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'PYTHONPATH=application .venv/bin/python -m pytest -v application/tests/'
            }
        }
    }
}
