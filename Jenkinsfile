pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/MehulPanditaGit/mlops_assignment.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mehulpanditadocker/mlops-model:pipeline .'
            }
        }
        
        stage('Run Model') {
            steps {
                bat 'docker run mehulpanditadocker/mlops-model:pipeline'
            }
        }
    }
}