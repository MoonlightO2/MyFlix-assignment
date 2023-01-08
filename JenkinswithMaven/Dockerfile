# Version: 0.0.1
FROM jenkins/jenkins:lts
MAINTAINER Andy C “aecobley@dundee.ac.uk”
USER root
RUN uname --kernel-name --kernel-release --machine
RUN apt-get -y update
RUN apt-get -y install maven
RUN apt-get -y install  wget
RUN apt-get -y install software-properties-common
RUN apt-get -y install python3.9
RUN apt-get install -y curl gnupg 
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add -
RUN apt-get update -y
RUN apt-get install google-cloud-sdk -y
USER jenkins
ENV PATH=$PATH:/google-cloud-sdk/bin
EXPOSE 80
EXPOSE 8080
EXPOSE 50000 
