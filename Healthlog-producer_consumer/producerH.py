from kafka import KafkaProducer
from pymongo import MongoClient

connecturl = "mongodb://127.0.0.1:27017/"

print("Connecting to mongodb server")
connection = MongoClient(connecturl)

db = connection.Health_Log

hospitals = db.mongodb_glossary


producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


def writedb():
    file1 = open('Hospitals.txt', 'r')
    Lines = file1.readlines()
    i=1
    for line in Lines:
        print("Message Sent ",i)
        producer.send('TestTopic',line.encode('utf-8'))
        i=i+1

def readdb():
    docs = db.hospitals.find()
        
    for document in docs:
        print(document)
        
num=0
while(num!=1):
    print("      MENU      ")
    print("1.Read Collection Hospital" )
    print("2.Write in Collection Hospital" )
    print("3.Exit")
    inp=int(input("Enter the opertation to be performed : "))
    if(inp==1):
        readdb()
    elif(inp==2):
        writedb()
    elif(inp==3):
        num=1
    else:
        print("Wrong option")
    
print("Closing the connection.")
connection.close()
producer.close()


