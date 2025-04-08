
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'stock-data',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Escuchando mensajes en 'stock-data'...")
for msg in consumer:
    print(f"Recibido: {msg.value}")
