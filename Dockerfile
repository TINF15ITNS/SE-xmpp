FROM rroemhild/ejabberd


ADD /auth.py /opt/ejabberd/scripts/lib/auth_mysql.py


#USER root

#RUN apt-get update -y && apt-get install -y python-pip
#Run apt-get install -y gcc python-dev
#RUN python -m pip install pymongo==2.7
#USER ejabberd

CMD ["start"]
ENTRYPOINT ["run"]