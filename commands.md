# Build container

```bash
docker build -t tinf15itns/ejabberd:v1 .
```

# Run container
```bash
docker run --name "ejabberd" \
-p 5222:5222 \
-p 5269:5269 \
-p 5280:5280 \
-h 'localhost' \
-e "EJABBERD_AUTH_METHOD=external" \
-e "EJABBERD_EXTAUTH_PROGRAM=/opt/ejabberd/scripts/lib/auth_mysql.py" \
-e "EJABBERD_EXTAUTH_INSTANCES=3" \
-e "EJABBERD_EXTAUTH_CACHE=600" \
-e "XMPP_DOMAIN=localhost" \
-e "ERLANG_NODE=ejabberd" \
-e "TZ=Europe/Berlin" \
tinf15itns/ejabberd:v1
```

# Look inside the container
```bash
docker exec -t -it ejabberd /bin/bash
```
