FROM rroemhild/ejabberd


ADD /authNikolai.py /opt/ejabberd/scripts/lib/auth_mysql.py

COPY /friendscomm.yml.sample /etc/friendscomm.yml.sample

USER root

#RUN apt-get update -y && apt-get install -y python-pip
#Run apt-get install -y gcc python-dev
#RUN python -m pip install pymongo==2.7


USER ejabberd

#öffnet Container-Ports für Kommunikation in der Docker-Bridge zwischen Container. Aus Container raus z.B. Internet oder Host sollte ohne weitere Einstellungen möglich sein. Wenn ein Container-Applikation auf einem Port horscht, dann müüsen anfragen von außerhalb an den Host-Port an den Container-Port weitergeleitet werden über "-p containerPort:HostPort" (oder andersrum) 
EXPOSE 80 27017