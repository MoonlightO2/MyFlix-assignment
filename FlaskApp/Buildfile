docker build -t flaskapp .
docker tag flaskapp acobley/flaskapp
docker push acobley/flaskapp
docker stop flaskapp
docker rm flaskapp
docker stop some-mysql
docker rm some-mysql
docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=dacjd156n. -d mysql:8.0
docker run -p 80:5000 -d --name flaskapp --link some-mysql:some-mysql acobley/flaskapp
