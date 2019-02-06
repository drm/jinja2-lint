FROM alpine:latest

RUN apk add --no-cache python py-jinja2
RUN mkdir -p /check

ADD j2lint.py /
ADD init.sh /
ENV CUSTOMLINT=customj2lint.py

CMD ["/usr/bin/env", "sh", "/init.sh"]