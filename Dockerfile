FROM alpine:latest

USER root
RUN apk add --no-cache coreutils findutils && \
    apk add --no-cache py3-pip py3-cffi py3-cryptography py3-ipaddr py3-ipaddress py3-jinja2 py3-markupsafe py3-netaddr py3-yaml && \
    pip3 install --no-cache-dir "ansible>=2.10,<2.11" jinja2-ansible-filters && \
    apk del --no-cache py3-pip && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    mkdir -p /check

COPY j2lint.py /
COPY init.sh /
ENV CUSTOMLINT=customj2lint.py


CMD ["/usr/bin/env", "sh", "/init.sh"]
