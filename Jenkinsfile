//Devops-Project-Joseph-Agam-Elbitsystems
node('docker') {
    stage('Checkout') {
    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/lordagam/Devops-Project-Joseph-Agam-Elbitsystems.git']])
    }
    stage('Python Flask App-Build & Push') {
        withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'pass', usernameVariable: 'user')]) {
     sh 'cd /root/jenkins/workspace/ect-Joseph-Agam-Elbitsystem_main/app && docker build -t lordagam/app  .'
     sh "sleep 10"
     sh 'docker images &&  docker ps'
     sh "sleep 5"
     sh "docker login -u $user -p $pass"
     sh 'docker push lordagam/app'
     echo 'finishes successfully'
     sh "sleep 5"
            }

    }
    stage('Nginx-Build & Push') {
        withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'pass', usernameVariable: 'user')]) {
     sh 'cd /root/jenkins/workspace/ect-Joseph-Agam-Elbitsystem_main/nginx && pwd && ls &&  docker build -t lordagam/nginx  .'
     sh "sleep 5"
     sh 'docker images &&  docker ps'
     sh "sleep 5"
     sh "docker login -u $user -p $pass"
     sh 'docker push lordagam/nginx'
     echo 'finishes successfully'
     sh "sleep 5"
            }

    }
    stage('A third Job Runs & Test') {
     sh 'docker compose up -d --build'
     sh 'docker images &&  docker ps'
     sh "sleep 10"
     sh 'curl localhost:80'
     echo 'finishes successfully'

    }    

    stage('successfully') {
     echo 'request has gone ok  and finishes successfully'


    }
}
