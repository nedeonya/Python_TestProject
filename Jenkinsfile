pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/demchenko23/Python_TestProject.git']])
            }
        }
        stage('build') {
            steps {
                git 'https://github.com/demchenko23/Python_TestProject.git'
            }
        }
        stage('test') {
            steps{
                 bat '''py -m pip install --user virtualenv
                        py -m venv test-venv
                        call ./test-venv/Scripts/activate.bat
                        pip install -r requirements.txt
                        python -m pytest --junit-xml=xmlreport.xml'''
            }
        }

    }
    post {
        always {
           junit 'xmlreport.xml'
        }
    }
}