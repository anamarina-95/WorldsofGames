pipeline {
    agent any
    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'GHJ1',
                    url: 'https://github.com/anamarina-95/WorldsofGames.git'
            }
        }
        stage('Build docker image') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Run the dockerized application') {
            steps {
                sh 'docker-compose run -d -p 8777:30000 -v "$(pwd)"/Scores.txt:/Scores.txt:ro \'
            }
        }
        stage('Test with Selenium the scores web service. Pipeline fails if tests fails') {
            steps {
                sh 'mvn clean install'
                sh 'mvn test'
                sh 'pytest --headless'
            }
        }
        stage('Finalize terminate the test container and push to DockerHub the new image created') {
            steps {
                sh 'docker-compose stop'
              withCredentials([usernamePassword(credentialsId: 'DHJ1', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          	sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          	sh 'docker push anamarina95/scores-app'
          	sh 'docker logout'
              }
            }
        }
    }
}
