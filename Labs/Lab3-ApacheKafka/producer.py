from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send some test events
producer.send('sample', b'Hello, CSYE7245!')
producer.send('sample', key=b'message-two', value=b'Kafka in use!')
producer.flush()