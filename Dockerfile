FROM alpine:latest

RUN apk add --no-cache python3 py3-requests
ADD vault-to-env.py /

ENTRYPOINT python3 /vault-to-env.py
 
