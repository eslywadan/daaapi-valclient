FROM python

RUN mkdir /service
WORKDIR /service
ENV PYTHONPATH=/service
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 23335
COPY . .
WORKDIR /service
ENTRYPOINT [ "python", "valclient_server.py"]

