FROM python:3.8

WORKDIR /app
ADD python-flask/requirements.txt .
RUN pip install -r requirements.txt
ADD python-flask/main.py .
ADD python-libs .

CMD FLASK_APP=main.py flask run --host=0.0.0.0 -p 80