FROM python:3.8.3
ENV PYTHONNUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt