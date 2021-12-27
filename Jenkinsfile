// Basic Jenkinsfile for Research
pipeline {
    agent any
    // This is where you would define your environment variables
    environment{
        NEW_VERSION = '1.1.0'
        SERVER_CREDENTIALS = credentials('server-admin')
    }
    // Build Tools for your Project
    // tools{

    // }
    parameters{
        string(name: 'VERSION', defaultValue: '', description: 'Version to deploy on prod')
        choice(name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: '')
        booleanParam(name: 'executeTest', defaultValue: true, description: '')
    }
    stages {
        stage("init"){
            steps{
                script{
                    gv = load "script.groovy"
                }
            }
        }
        stage("build"){
            steps{
                script{
                    gv.buildApp()
                }
            }
        }
        stage("test"){
            when {
                // if current branch is dev
                expression{
                    // BRANCH_NAME == 'dev' || BRANCH_NAME == 'main'
                    params.executeTest
                }
            }
            steps{
                script{
                    gv.testApp()
                }
            }
        }
        stage("deploy"){
            steps{
                script{
                    gv.deployApp()
                }
            }   
        }
    }
    // Executes Scripts After Stages are Complete
    post{
        // Executed always regardless of success/failure
        always{
            echo "Script Complete"
        }
        success{
            echo "Script Successful"
        }
        failure{
            echo "Script Failed"
        }
    }
}
