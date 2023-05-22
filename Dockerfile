FROM python

COPY . /docker-example
WORKDIR /docker-example

RUN pip install flask


EXPOSE 9595

CMD ["python","main.py"]



