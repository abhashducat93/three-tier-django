pipeline {
    agent any
    
    environment {
        APP_NAME = 'three-tier-django'
        COMPOSE_FILE = 'docker-compose.yml'
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/yourusername/three-tier-django.git'
            }
        }
        
        stage('Build Application') {
            steps {
                dir('app') {
                    sh 'docker build -t ${APP_NAME}-app:latest .'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                dir('app') {
                    sh '''
                    docker run --rm \
                    -e DB_NAME=testdb \
                    -e DB_USER=testuser \
                    -e DB_PASSWORD=testpass \
                    -e DB_HOST=localhost \
                    ${APP_NAME}-app:latest \
                    python manage.py test --noinput
                    '''
                }
            }
        }
        
        stage('Deploy to Staging') {
            steps {
                sh 'docker-compose -f ${COMPOSE_FILE} down || true'
                sh 'docker-compose -f ${COMPOSE_FILE} up -d --build'
            }
        }
        
        stage('Health Check') {
            steps {
                sh 'sleep 15'
                sh 'curl -f http://localhost:8080/health/ || exit 1'
                sh 'curl -f http://localhost:8080/ || exit 1'
            }
        }
    }
    
    post {
        always {
            sh 'docker system prune -f || true'
            cleanWs()
        }
        
        success {
            echo 'Three-tier deployment successful!'
            echo 'Access your app at: http://localhost:8080'
        }
        
        failure {
            echo 'Deployment failed! Check logs for details.'
            sh 'docker-compose -f ${COMPOSE_FILE} logs'
        }
    }
}
