FROM rroemhild/ejabberd


ADD /extauth/auth.py /opt/ejabberd/scripts/lib/auth_mysql.py

ADD /friendscomm.yml /etc/friendscomm.yml

USER root

RUN apt-get update -y && apt-get install -y python-pip
Run apt-get install -y gcc python-dev
RUN python -m pip install pymongo==2.7
RUN python -m pip install pyjwt==2.7
#RUN python -m pip install pyyaml
RUN mkdir /var/log/ejabberd
RUN chown ejabberd:ejabberd /var/log/ejabberd


USER ejabberd

#öffnet Container-Ports für Kommunikation in der Docker-Bridge zwischen Container. Aus Container raus z.B. Internet oder Host sollte ohne weitere Einstellungen möglich sein. Wenn ein Container-Applikation auf einem Port horscht, dann müüsen anfragen von außerhalb an den Host-Port an den Container-Port weitergeleitet werden über "-p containerPort:HostPort" (oder andersrum) 
#EXPOSE 80 27017
