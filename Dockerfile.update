# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-slim-buster

WORKDIR /usr/src/PyIPAM
#EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

#RUN apt-get update
#RUN apt-get install gcc -y
#RUN apt-get clean

RUN pip install --upgrade pip

# Install pip requirements
COPY ./requirements.txt /usr/src/PyIPAM/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/PyIPAM/

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /usr/src/PyIPAM
USER appuser

#RUN python -m flask db migrate
#RUN python -m flask db upgrade

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "PyIPAM:app"]


#FROM python:3.6

#ENV FLASK_APP PyIPAM.py

#COPY PyIPAM.py gunicorn-cfg.py requirements.txt ./
#COPY app app

#RUN pip install -r requirements.txt

