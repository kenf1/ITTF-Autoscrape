#setup container
FROM python:3.11.6-slim
COPY ./app ./app

#install packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r ./app/requirements.txt

#run app
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["python3","-m","streamlit","run","./app/Home.py","--server.port=8501","--server.address=0.0.0.0"]
