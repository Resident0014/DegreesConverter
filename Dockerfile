FROM python:3.10

ADD DegreesConverter.py /
CMD [ "python3", "./DegreesConverter.py" ]