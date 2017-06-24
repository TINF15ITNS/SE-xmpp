FROM rroemhild/ejabberd
MAINTAINER Nikolai Seip

ENV EJABBERD_HOME=/opt/ejabberd \
	XMPP_DOMAIN=localhost \
	EJABBERD_AUTH_METHOD=external \
	EJABBERD_EXTAUTH_PROGRAM="/opt/ejabberd/scripts/lib/auth.py" \
	EJABBERD_EXTAUTH_INSTANCES=3 \
	EJABBERD_EXTAUTH_CACHE=600 \
	ERLANG_NODE=ejabberd \
	EJABBERD_ADMINS=admin@localhost \
	EJABBERD_USERS=admin@localhost:admin \
	TZ=Europe/Berlin
	
	

COPY /extauth/auth.py /opt/ejabberd/scripts/lib/auth.py

CMD ["start"]
ENTRYPOINT ["run"]
