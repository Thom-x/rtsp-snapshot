# RTSP Snapshot

[![Build Status](https://travis-ci.org/Thom-x/rtsp-snapshot.svg?branch=master)](https://travis-ci.org/Thom-x/rtsp-snapshot)
![](https://images.microbadger.com/badges/image/thomx/rtsp-snapshot.svg)
![](https://images.microbadger.com/badges/version/thomx/rtsp-snapshot.svg)
![GitHub](https://img.shields.io/github/license/Thom-x/rtsp-snapshot)

Simple docker image to grab snapshot from a RTSP stream.

## Getting Started

These instructions will cover usage information and for the docker container 

### Prerequisities

In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### Usage

#### Container Parameters

Run the image

```shell
docker run -v "/path/to/snapshot/on/host:/var/www/localhost/htdocs/snapshots" -e URL=rtsp://192.168.1.63/unicast -p 80:80 thomx/rtsp-snapshot
```

Take a snapshot :

http://localhost/snapshot.cgi

List snapshots :

http://localhost/snapshots

#### Environment Variables

* `URL` - URL of the stream to grap snapshot from

#### Volumes

* `/var/www/localhost/htdocs/snapshots` - Snapshot folder location

## Built With

* mini_httpd 1.23-r1
* ffmpeg 2.8.11-r0

## Find Me

* [GitHub](https://github.com/Thom-x/)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the 
[tags on this repository](https://github.com/your/repository/tags). 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
