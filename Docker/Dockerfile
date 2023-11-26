FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y openssh-server iproute2 iputils-ping python3-pip
RUN pip3 install pyyaml

COPY ./ /root
RUN mkdir /data
WORKDIR /root
