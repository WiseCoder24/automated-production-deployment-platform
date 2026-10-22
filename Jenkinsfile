
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
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                        -t devops-status-app:1.0.0 \
                        -f application/Dockerfile \
                        application
                '''
            }
        }
        stage('Push to AWS ECR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'aws-ecr-credentials',
                    usernameVariable: 'AWS_ACCESS_KEY_ID',
                    passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                )]) {
                    sh '''
                        set -e

                        export AWS_ACCESS_KEY_ID
                        export AWS_SECRET_ACCESS_KEY
                        export AWS_DEFAULT_REGION=us-east-1

                        ECR_REGISTRY="721366939861.dkr.ecr.us-east-1.amazonaws.com"
                        ECR_REPOSITORY="automated-production-deployment-platform"
                        IMAGE_TAG="1.0.0"

                        aws ecr get-login-password --region "$AWS_DEFAULT_REGION" \
                          | docker login --username AWS --password-stdin "$ECR_REGISTRY"

                        docker tag devops-status-app:$IMAGE_TAG \
                          "$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG"

                        docker push "$ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG"
                    '''
                }
            }
        }
    }
}
