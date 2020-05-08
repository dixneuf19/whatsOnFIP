FROM python:3.8

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src src

ENTRYPOINT [ "uvicorn", "src.main:app" , "--host", "0.0.0.0"]