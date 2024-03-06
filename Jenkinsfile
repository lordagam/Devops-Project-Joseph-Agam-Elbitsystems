pipeline {
  agent {
    node {
      label 'centos-docker'
    }

  }
  stages {
    stage('checkout') {
      steps {
        git(url: 'https://github.com/lordagam/Devops-Project-Joseph-Agam-Elbitsystems.git', branch: 'main')
        echo 'finishes successfully'
      }
    }

    stage('Python Flask App-Build & Push') {
      steps {
        sh 'cd /root/jenkins/workspace/ect-Joseph-Agam-Elbitsystem_main/app && docker build -t lordagam/app  .'
        sh 'docker images &&  docker ps'
        sh ' docker tag devops-project-joseph-agam-elbitsystems-app  lordagam/app'
        sleep 5
        sh 'docker login -u $user -p $pass'
        sh 'docker push lordagam/app:$BUILD_NUMBER'
        echo 'finishes successfully'
      }
    }

    stage('Nginx-Build & Push') {
      steps {
        sh 'cd /root/jenkins/workspace/ect-Joseph-Agam-Elbitsystem_main/nginx && pwd && ls &&  docker build -t lordagam/nginx  .'
        sh 'docker images &&  docker ps'
        sh 'docker tag devops-project-joseph-agam-elbitsystems-nginx  lordagam/nginx'
        sleep 5
        sh 'docker login -u $user -p $pass'
        sh 'docker push lordagam/nginx:$BUILD_NUMBER'
        echo 'finishes successfully'
      }
    }

    stage('A third Job Runs') {
      steps {
        sh 'docker compose up -d --build'
        echo 'finishes successfully'
      }
    }

    stage(' successfully') {
      steps {
        echo 'request has gone ok  and finishes successfully'
      }
    }

  }
}