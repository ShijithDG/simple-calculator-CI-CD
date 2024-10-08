pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            // args '-u root'
        }
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/ShijithDG/simple-calculator-CI-CD.git' // Replace with your repository URL
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t simple-calculator .'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run tests using the built image
                    sh 'git status'
                    sh 'docker run --rm simple-calculator'
                }
            }
        }
    }
    post {
        always {
            // Clean up workspace
            cleanWs()
        }
    }
}
