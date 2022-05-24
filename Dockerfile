FROM alpine:latest

USER root
RUN apk add --no-cache ansible py3-pip coreutils findutils && \
    pip3 install --no-cache-dir ipaddr jinja2-ansible-filters && \
    ln -s /usr/bin/python3 /usr/bin/python && \
    mkdir -p /check

COPY j2lint.py /
COPY init.sh /
ENV CUSTOMLINT=customj2lint.py

USER nobody

CMD ["/usr/bin/env", "sh", "/init.sh"]
