# Build
$ docker build -t simple_app .

# Run
$ docker run -d -e APP_SETTINGS="config.ProductionConfig" -e DATABASE_URL="postgresql://<user>:<password>@<host>/simple_app" -p 5123:5123 simple_app

$ curl http://localhost:5123/
$ curl http://localhost:5123/messages
$ curl -X POST http://localhost:5123/messages/hoge
