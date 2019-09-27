FROM python:3.7
RUN pip install pipenv
WORKDIR /usr/local/serverless/serverless
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install