pipeline {
  agent any
  stages {
    stage('Stage') {
      steps{
      bat 'call stage.bat'     
      }
    }
     stage('Confirmation') {
      steps{
      input ''
      }
    }
    stage('Deploy') {
      steps{
      bat 'call deploy.bat'     
      }
    }
    stage('Archive') {
      steps {
         archiveArtifacts '*'
          }
    }
     stage('Archive') {
      steps {
         fingerprint '/'
          }
    }
  }
}
