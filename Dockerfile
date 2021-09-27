FROM python:3.9
WORKDIR /usr/local/serverless
COPY serverless /usr/local/serverless
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python", "manage.py",  "runserver", "0.0.0.0:80"]