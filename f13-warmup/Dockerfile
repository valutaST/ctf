FROM ruby:3
RUN apt update -y; apt install -y supervisor
RUN gem install webrick erb

RUN useradd -ms /bin/bash f13

RUN mkdir -p /app
WORKDIR /app

COPY flag.txt /flag.txt

RUN chown f13:f13 /flag.txt
RUN chmod 400 /flag.txt  

COPY app .
COPY config/supervisord.conf /etc/supervisord.conf

EXPOSE 30002

ENTRYPOINT [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf" ]
