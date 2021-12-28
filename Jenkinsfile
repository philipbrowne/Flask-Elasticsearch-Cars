pipeline {
   agent any
   stages{
      stage ('Assemble Containers') {
         steps{
            sh "docker-compose up -d"
            echo "Docker Containers Running"
            }
      }
      stage ('Run Tests') {
         steps{
            // Basic Single View Test for 200 Status Code
            sh 'docker exec -i carspipeline_web_1 /bin/sh -c "cd /var/www/app && python3 -m unittest"'
            }
         }
      stage ('Shutdown Containers'){
         steps{
            sh "docker-compose down"
         }
      }
   }
}