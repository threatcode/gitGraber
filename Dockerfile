FROM python:latest

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/hisxo/gitGraber
WORKDIR /gitGraber
RUN pip install -r requirements.txt

ENTRYPOINT ["python","gitGraber.py"]
CMD ["--help"]
