FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN echo 'nameserver 8.8.8.8'>/etc/resolv.conf
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/main.py"]
