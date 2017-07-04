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
-v ~/ssl:/opt/ejabberd/ssl \
-h 'localhost' \
-e "XMPP_DOMAIN=localhost" \
-e "TZ=Europe/Berlin" \
--env-file env.list
tinf15itns/ejabberd:v1
```

# Look inside the container
```bash
docker exec -t -it ejabberd /bin/bash
```
