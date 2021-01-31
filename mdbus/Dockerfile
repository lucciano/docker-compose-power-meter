FROM arm32v6/alpine:3.12.3
RUN apk update && \
    apk upgrade && \
    apk --update add \
        gcc \
        g++ \
        build-base \
        cmake \
        bash \
	git \
	pkgconfig \
        libstdc++ && \
    rm -rf /var/cache/apk/* 

RUN  git clone https://github.com/3cky/mbusd.git mbusd.git
RUN  cd mbusd.git && mkdir -p build && cd build && cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make && make install
