FROM python:latest
COPY trader.py /
CMD [ "python", "./trader.py" ]
