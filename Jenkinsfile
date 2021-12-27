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
        stage("build"){
            steps{
                when {
                // if current branch is dev
                expression{
                    BRANCH_NAME == 'dev' || BRANCH_NAME == 'main' && CODE_CHANGES
                }
            }
                echo "Code Changes Detected..."
                // Needs to be in double quotes to use variable in string
                echo "Building the Application ${NEW_VERSION}"
            }
        }
        stage("test"){
            when {
                // if current branch is dev
                expression{
                    // BRANCH_NAME == 'dev' || BRANCH_NAME == 'main'
                    params.executeTests
                }
            }
            steps{
                echo "Testing the Application..."
            }
        }
        stage("deploy"){
            steps{
                echo "Deploying the Application"
                withCredentials([usernamePassword(credentials: 'server-admin', usernameVariable: USER, passwordVariable: PWD)])
                echo "Deploying As ${SERVER_CREDENTIALS}"
                echo "SOME SCRIPT WITH ${USER} and ${PWD}"
                echo "Deploying version ${params.VERSION}"
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
