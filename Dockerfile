FROM python:3.7
RUN pip install pipenv
WORKDIR /usr/local/serverless/serverless
#COPY Pipfile .
#COPY Pipfile.lock .
COPY requirements.txt .
RUN pip3 install -r requirements.txt