FROM python:2.7
RUN apt-get update
RUN apt-get install python-pip iputils-ping -y 
ADD ./flask_blog /app 
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python",  "runserver.py"]

