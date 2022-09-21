pipeline {
  agent any
  environment {
  AWS_ACCOUNT_ID= "519927740453"
  AWS_DEFAULT_REGION = "us-east-1"
  IMAGE_REPO_NAME = "takehome-ecr"
  IMAGE_TAG = "latest"
  REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
  }
  stages {
    stage('create docker image') {
      steps {
        script {
          docker.withRegistry("519927740453.dkr.ecr.us-east-1.amazonaws.com/takehome-ecr", "ecr:us-east-1:67dd93aa-0158-4343-808c-a07957103457") {
            docker.image("takehome-app").push()
          }
        }
      }
    }

  // Uploading Docker images into AWS ECR
    stage('Pushing to ECR') {
      steps {
        script {
          sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
          sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
        }
      }
    }
  }
}
