pipeline {
  agent any
  environment {
    registry = "519927740453.dkr.ecr.us-east-1.amazonaws.com/takehome-ecr"
  }
  stages {
    stage('create docker image') {
      steps {
        script {
          dockerimage = docker.build registry
          }
        }
      }
    }

  // Uploading Docker images into AWS ECR
    stage('Pushing to ECR') {
      steps {
        script {
          sh 'aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 519927740453.dkr.ecr.us-east-1.amazonaws.com'
          sh 'docker push 519927740453.dkr.ecr.us-east-1.amazonaws.com/takehome-ecr:latest'
        }
      }
    }
  }
}
