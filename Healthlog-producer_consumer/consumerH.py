from kafka import KafkaConsumer
from pymongo import MongoClient


connecturl = "mongodb://127.0.0.1:27017/"

print("Connecting to mongodb server")
connection = MongoClient(connecturl)

db = connection.Health_Log

hospitals = db.mongodb_glossary

consumer = KafkaConsumer('TestTopic',bootstrap_servers=['localhost:9092'])

for message in consumer:
    print(message.value.decode("utf-8"))
    x=message.value.decode("utf-8").split()
    d={x[0]:x[1],x[2]:x[3],x[4]:x[5],x[6]:x[7],x[8]:x[9],x[10]:x[11],x[12]:x[13]}
    db.hospitals.insert_one(d)    
    
print("Closing the connection.")
connection.close()
consumer.close()
