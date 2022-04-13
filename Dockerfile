FROM python:3.11.0a7-slim
LABEL maintainer="Project Pluto"

WORKDIR /usr/src/app
RUN pip install --upgrade pip; pip install wheel

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app/
EXPOSE 8000
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload" ]
