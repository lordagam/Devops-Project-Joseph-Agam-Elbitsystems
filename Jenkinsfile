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
            echo 'good '
          }
        }

        stage('pwd') {
          steps {
            sh 'ls && pwd'
          }
        }

      }
    }

    stage('Build') {
      steps {
        sh 'ls && pwd'
        sh 'cd /root/jenkins/workspace/ect-Joseph-Agam-Elbitsystem_main/app && docker build -t lordagam/app  .'
        sh 'docker images &&  docker ps'
        sh 'cd /root/jenkins/workspace/ect-Joseph-Agam-Elbitsystem_main/nginx && pwd && ls &&  docker build -t lordagam/nginx  .'
        sh 'ls && pwd'
        sh 'docker images &&  docker ps'
        echo 'Hello from Chuck Norris'
      }
    }

    stage('push to dockerhub') {
      steps {
        sh 'docker tag docker tag devops-project-joseph-agam-elbitsystems-app:$BUILD_NUMBER  lordagam/app'
        sh 'docker tag docker tag devops-project-joseph-agam-elbitsystems-nginx:$BUILD_NUMBER  lordagam/nginx'
        sh '"docker login -u $user -p $pass"'
        sleep 5
        sh '"docker push lordagam/app:$BUILD_NUMBER"'
        sh '"docker push lordagam/nginx:$BUILD_NUMBER"'
      }
    }

  }
}