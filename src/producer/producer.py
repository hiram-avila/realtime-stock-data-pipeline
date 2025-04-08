from kafka import KafkaProducer
import yfinance as yf
import json
import time

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

ticker = 'AAPL'
data = yf.Ticker(ticker).history(period="5d", interval="1m")

for index, row in data.iterrows():
    mensaje = {
        'ticker': ticker,
        'timestamp': str(index),
        'open': row['Open'],
        'high': row['High'],
        'low': row['Low'],
        'close': row['Close'],
        'volume': row['Volume']
    }
    print(f"Enviando: {mensaje}")
    producer.send('stock-data', mensaje)
    time.sleep(1)

producer.flush()
