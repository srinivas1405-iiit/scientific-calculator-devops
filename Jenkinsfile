pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = "srinivas1405/scientific-calculator"
        DOCKER_TAG = "${BUILD_NUMBER}"
        DOCKER_CREDENTIALS = 'dockerhub-credentials'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    pytest test_calculator.py -v --cov=calculator --cov-report=html --cov-report=term
                '''
            }
            post {
                always {
                    echo 'Archiving test results...'
                    junit skipPublishingChecks: true, testResults: '**/test-results/*.xml', allowEmptyResults: true
                }
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                '''
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing Docker image to Docker Hub...'
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS) {
                        sh '''
                            docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                            docker push ${DOCKER_IMAGE}:latest
                        '''
                    }
                }
            }
        }
        
        stage('Deploy with Ansible') {
            steps {
                echo 'Deploying application using Ansible...'
                sh '''
                    ansible-playbook -i inventory.ini deploy.yml --extra-vars "docker_image=${DOCKER_IMAGE}:latest"
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Cleaning up...'
            sh 'docker system prune -f'
        }
    }
}
