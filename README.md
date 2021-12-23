# Cars API with ElasticSearch and RabbitMQ

Make Sure Docker is Installed on Your Machine

To Start Local Deployment:
`docker-compose up`

Wait for ElasticSearch to initialize - it can sometimes take 20-30 seconds.

To Get All Cars - Make GET Request to 'localhost:8000/'

To Create Car - Make POST Request to 'localhost:8000/' with Valid JSON Schema
{
"make" : "text",
"model": "text",
"color": "text",
"year" : "integer"
}

To Search Cars - Make GET Request to '/search' with following search keywords in JSON Body
{"make", "model", "color", "year"}

To Get Car By Id - Make GET Request to '/{id}'

To Update Car by Id - Make PUT Request to '/{id}' with Valid JSON Schema containing one of the following:
{
"make" : "text",
"model": "text",
"color": "text",
"year" : "integer"
}

To Delete Car By Id - Make DELETE Request to '/{id}'

RabbitMQ Logs Can Be Seen in Terminal
