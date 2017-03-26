pipeline {
  agent any
  stages {
    stage('Messge') {
      steps {
        echo 'Welcome'
      }
    }
    stage('Archive') {
      steps {
        parallel(
          "Archive": {
            archiveArtifacts '*'
            
          },
          "Fingerprints": {
            fingerprint '*'
            
          }
        )
      }
    }
  }
}