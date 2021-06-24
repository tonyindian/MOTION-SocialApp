FROM continuumio/miniconda3:latest

RUN apt-get update && apt-get upgrade -y && apt-get install -qqy \
        wget \
        bzip2 \
        graphviz

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs && apt-get install -y npm

COPY ./app/requirements.yml /app/requirements.yml

RUN /opt/conda/bin/conda env create -f /app/requirements.yml

ENV PATH /opt/conda/envs/django_motion/bin:$PATH

RUN echo "source activate django_motion" >~/.bashrc

COPY ./scripts /scripts
RUN chmod +x ./scripts*

COPY ./app /app

RUN mkdir -p /frontend
RUN mkdir -p /frontend_temp
WORKDIR frontend_temp
COPY ./frontend/package.json /frontend_temp/
RUN npm install
COPY ./frontend /frontend_temp
RUN npm run build

WORKDIR /app

