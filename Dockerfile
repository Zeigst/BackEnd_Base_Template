FROM python:3.12

WORKDIR /app

RUN pip install --upgrade pip

ADD requirements.txt .

RUN python -m pip install -r requirements.txt

ADD . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]