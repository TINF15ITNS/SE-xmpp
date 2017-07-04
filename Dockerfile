FROM rroemhild/ejabberd

COPY /extauth/auth.py /opt/ejabberd/scripts/lib/auth.py

COPY /friendscomm.yml /etc/friendscomm.yml


USER root

RUN apt-get update -y && apt-get install -y python-pip python-dev
RUN python -m pip install pymongo==2.7
RUN python -m pip install pyjwt
RUN python -m pip install pyyaml

RUN mkdir /var/log/ejabberd
RUN chown -R ejabberd:ejabberd /var/log/ejabberd

USER ejabberd

RUN touch /var/log/ejabberd/crash.log
RUN touch /var/log/ejabberd/error.log
RUN touch /var/log/ejabberd/erlang.log
