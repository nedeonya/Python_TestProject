pipeline {
    agent any
    parameters {
        choice(name: 'TYPE', choices: ['ALL', 'UI', 'API'])
        booleanParam (name: 'executeTests', defaultValue: true)
    }
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
        stage('ALL tests') {
            when {
                expression {
                    params.executeTests && params.TYPE == 'ALL'
                }
            }
            steps {
                 bat '''py -m pip install --user virtualenv
                        py -m venv test-venv
                        call ./test-venv/Scripts/activate.bat
                        pip install -r requirements.txt
                        python -m pytest --junit-xml=xmlreport.xml'''
            }
        }
        stage('UI tests') {
            when {
                expression {
                    params.executeTests && params.TYPE == 'UI'
                }
            }
            steps {
                 bat '''py -m pip install --user virtualenv
                        py -m venv test-venv
                        call ./test-venv/Scripts/activate.bat
                        pip install -r requirements.txt
                        python -m pytest tests/ui_tests/ --junit-xml=xmlreport.xml'''
            }
        }
    }
    post {
        always {
           junit 'xmlreport.xml'
        }
    }
}