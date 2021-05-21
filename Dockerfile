FROM python:3.7.9
RUN pip3 install pandapower
WORKDIR /app
COPY ["test.py", "/app/"]
ENTRYPOINT ["python", "-u", "test.py"]

