FROM alpine:latest

USER root
RUN apk add --no-cache ansible
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN mkdir -p /check

COPY j2lint.py /
COPY init.sh /
ENV CUSTOMLINT=customj2lint.py

USER nobody

CMD ["/usr/bin/env", "sh", "/init.sh"]

