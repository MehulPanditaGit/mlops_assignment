pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'YOUR_GITHUB_REPO_URL'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t YOUR_DOCKERHUB_ID/mlops-model:pipeline .'
            }
        }
        
        stage('Run Model') {
            steps {
                bat 'docker run YOUR_DOCKERHUB_ID/mlops-model:pipeline'
            }
        }
    }
}