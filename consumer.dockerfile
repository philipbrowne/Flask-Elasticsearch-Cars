FROM rabbitmq:management-alpine
COPY consumer.py .
RUN apk --update --no-cache add python3-dev && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install pika
EXPOSE 5672
CMD ["python3", "-u", "consumer.py"]