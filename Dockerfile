FROM rroemhild/ejabberd


COPY /extauth/auth.py /opt/ejabberd/scripts/lib/auth_mysql.py

COPY /friendscomm.yml /etc/friendscomm.yml

USER root

RUN apt-get update -y && apt-get install -y python-pip python-dev
RuN python -m pip install pymongo==2.7
RUN python -m pip install pyjwt
RUN python -m pip install pyyaml
RUN mkdir /var/log/ejabberd
RUN touch /var/log/ejabberd/crash.log
RUN touch /var/log/ejabberd/error.log
RUN touch /var/log/ejabberd/erlang.log
RUN chown -R ejabberd:ejabberd /var/log/ejabberd

USER ejabberd

#öffnet Container-Ports für Kommunikation in der Docker-Bridge zwischen Container. Aus Container raus z.B. Internet oder Host sollte ohne weitere Einstellungen möglich sein. Wenn ein Container-Applikation auf einem Port horscht, dann müüsen anfragen von außerhalb an den Host-Port an den Container-Port weitergeleitet werden über "-p containerPort:HostPort" (oder andersrum) 
#EXPOSE 80 27017
