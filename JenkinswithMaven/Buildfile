docker build -t jenkinsmavengcloud .
docker tag jenkinsmavengcloud acobley/jenkinsmavengcloud
docker push acobley/jenkinsmavengcloud
docker stop jenkinsmavengcloud
docker rm jenkinsmavengcloud
docker run -p 80:8080 -p 50000:50000 -d --name jenkins acobley/jenkinsmavengcloud
