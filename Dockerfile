FROM python:3.6

WORKDIR /app

COPY requirements.txt /app
COPY populate_db.py /app
COPY data/globalLandTemperaturesByCountry.csv /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "populate_db.py"]