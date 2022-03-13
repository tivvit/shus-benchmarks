FROM python:latest

WORKDIR /app
ADD python-tornado/requirements.txt .
RUN pip install -r requirements.txt
ADD python-tornado/main.py .
ADD python-libs .

CMD python main.py