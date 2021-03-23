FROM ubuntu:latest
RUN apt update
RUN apt install -y python3-pip
WORKDIR /app/
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY app.py /app/
EXPOSE 9090
CMD ["python3","app.py"]



