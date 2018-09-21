FROM ubuntu:16.04
MAINTAINER Jeganathan Swaminathan <http://www.tektutor.org> <jegan@tektutor.org>

RUN apt-get update && apt-get install -y openssh-server && apt-get install -y python-minimal && apt-get install -y default-jdk && apt-get install -y maven
RUN mkdir /var/run/sshd

#Change the root user password to root
RUN echo 'root:root' | chpasswd

#This enables Root Login
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise the user will be kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

#Copy your public key i.e /root/id_rsa.pub as authorized_keys inside container
COPY authorized_keys /root/.ssh/authorized_keys

#This opens port 22 which is used by SSH Server, by default all ports are closed
EXPOSE 22

#This opens port 80 in container, we will use this port for nginx web server
EXPOSE 80 

#This configures start up application in a container
CMD ["/usr/sbin/sshd", "-D"]
