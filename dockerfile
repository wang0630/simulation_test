FROM python:3.8

ARG rootPath=/simulation_test

RUN mkdir -p ${rootPath}

WORKDIR ${rootPath}

COPY requirements.txt .

RUN python3 -m venv venv \
  && . venv/bin/activate \
  && pip3 install -r requirements.txt

COPY . .

CMD . venv/bin/activate && python3 -u main.py
