FROM ubuntu:18.04

COPY . /app
WORKDIR /app

# install google chrome
RUN apt-get update

RUN apt-get install -y wget gnupg ca-certificates procps libxss1 curl
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -      && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' 
RUN apt-get update 
RUN apt-get install -y google-chrome-stable 

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/
RUN ln -s /usr/local/bin/chromedriver && chmod 777 /usr/local/bin/chromedriver

# set display port to avoid crash
ENV DISPLAY=:99

RUN  apt-get install -y python3.8 python3-pip python3-venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["pytest", "-s" , "-v", "--browser", "chrome", "--html=report.html"]