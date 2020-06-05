FROM dseg/mini_httpd-cgi
MAINTAINER Maugin Thomas

RUN \
 apk add --update ffmpeg coreutils \
 &&\
 rm -rf /var/cache/apk/*

COPY rootfs /

# S6 OVERLAY
ADD https://github.com/just-containers/s6-overlay/releases/download/v1.21.8.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / && rm /tmp/s6-overlay-amd64.tar.gz

ENTRYPOINT ["/init"]