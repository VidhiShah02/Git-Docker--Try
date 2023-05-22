FROM python

COPY . /docker-example
WORKDIR /docker-example

RUN pip install flask
RUN pip install redis

EXPOSE 9595

CMD ["python","main.py"]



