pipeline {
  agent {
    node {
      label 'centos-docker'
    }

  }
  stages {
    stage('checkout') {
      parallel {
        stage('checkout') {
          steps {
            git(url: 'https://github.com/lordagam/Devops-Project-Joseph-Agam-Elbitsystems.git', branch: 'main')
          }
        }

        stage('Hello from Chuck Norris') {
          steps {
            echo 'good '
          }
        }

      }
    }

    stage('Build') {
      steps {
        sh 'ls && pwd'
        sh 'cd /app'
        sh '"docker build -t lordagam/app:$BUILD_NUMBER  ."'
        sh '"docker build -t lordagam/nginx:$BUILD_NUMBER  ."'
        echo 'Hello from Chuck Norris'
      }
    }

    stage('push to dockerhub') {
      steps {
        sh '"docker login -u $user -p $pass"'
        sleep 5
        sh '"docker push lordagam/app:$BUILD_NUMBER"'
        sh '"docker push lordagam/nginx:$BUILD_NUMBER"'
        sh '"docker tag docker tag devops-project-joseph-agam-elbitsystems-app:$BUILD_NUMBER  lordagam/app"'
      }
    }

  }
}