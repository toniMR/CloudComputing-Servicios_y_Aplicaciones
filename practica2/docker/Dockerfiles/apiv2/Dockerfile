FROM python:3.6

EXPOSE 8080

RUN useradd -m nonrootuser

WORKDIR /home/nonrootuser/practica2

COPY api/v2/apiv2.py ./
COPY api/v2/functions.py ./
COPY api/v2/requirements.txt ./

RUN pip3 install -r requirements.txt 

USER nonrootuser

CMD ["python3", "apiv2.py"]
