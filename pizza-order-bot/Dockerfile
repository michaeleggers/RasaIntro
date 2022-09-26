FROM rasa/rasa:latest

WORKDIR '/app'
COPY . /app

USER root

RUN rasa train

# RUN apt-get update && apt-get -y install sudo

# RUN adduser --disabled-password --gecos '' docker
# RUN adduser docker sudo
# RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# RUN sudo su
# RUN sudo apt-get install -y python3
# RUN sudo apt-get install -y python3-pip

# RUN sudo pip3 install -U --user pip && sudo pip3 install rasa

EXPOSE 5005
EXPOSE 5055
USER 1001

CMD ["run","-m","/app/models","--enable-api","--cors","*","--debug" ,"--endpoints", "/app/endpoints.yml", "--log-file", "out.log", "--debug"]
