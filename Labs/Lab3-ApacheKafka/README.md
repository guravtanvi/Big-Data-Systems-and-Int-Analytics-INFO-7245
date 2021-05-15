## Big Data Systems and Int Analytics

## Labs

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
|   Tanvi Gurav     |   001306848     |
|   Keerti Ojha     |   001050173     |
| Priyanka Malpekar |   001302741     |


## Lab 3 - Apache Kafka

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=18gjiG4BLFSI-kqlX1QL7PYNOW0s6KEOY7O972kxY0ME#0

### Lab Completion Date

5th February’21

## About

**This lab demonstrates leveraging and implementing Kafka services for static data along with  real-timeTwitter streaming.**
 
 ## Kafka

**Apache Kafka** is a streaming message platform. It is a publish-subscribe based durable messaging system. Kafka is designed to be high performance, highly available, and redundant. It is used to collect, process, store, and integrate data at scale. A messaging system sends messages between processes, applications, and servers. 

<img width="943" alt="Screen-Shot-2017-06-04-at-2-44-24-PM" src="https://user-images.githubusercontent.com/59594174/109214042-57a64b00-777f-11eb-8e93-472a4967cdd6.png">

It’s basic use cases includes:
- Stream Processing
- Messaging
- Website Activity Tracking
- Log aggregation
- Event Sourcing
- Application health monitoring

These are four main parts in a Kafka system:

- **Broker:** Handles all requests from clients (producer, consumer and metadata) and keeps data replicated within the cluster. There can be one or more brokers in a cluster
- **Zookeeper:** Keeps track of status of the Kafka clusters (brokers, topics, users)
- **Producer:** Sends records to a broker
- **Consumer:** Consumes batches of records from the broker

![Broker](https://user-images.githubusercontent.com/59594174/109211286-08125000-777c-11eb-99f7-1a3eaa5abce3.png)

## Requirements

1. Installing Oracle **Virtual VM Box**

![Oracle VM](https://user-images.githubusercontent.com/59594174/109211194-e618cd80-777b-11eb-8963-5d82188f2686.png)

**Specifications**
- Minimum 4 GB RAM
- Minimum 25 GB Hard Drive
- Downloading **ubuntu** iso file


2. Installing **Ubuntu** Guest Edition

`sudo apt install build-essential dkms linux-headers-$(uname -r)`

3. Installing Python on the Virtual VM

`sudo apt install python3`

4. Installing AWS CLI

```
sudo apt install curl

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install

/usr/local/bin/aws --version

```

5. Connecting with AWS

` aws configure`

6. Installing Java jdk

```
sudo apt install default-jre

sudo apt install default-jdk

```

7. Installing Pycharm in Ubuntu


## Test Results

#### Download & Configure Kafka
- Download Apache Kafka from [here](https://kafka.apache.org/downloads)

-Install the required pyhton libraries
`pip3 install kafka-python`


#### Starting Zookeeper & Kafka Broker

Navigate to the directory where the downloaded files are unzipped and start the **Zookeeper** service:
```
bin/zookeeper-server-start.sh config/zookeeper.properties
```
Additionally, start the **Kafka broker** by running:
```
bin/kafka-server-start.sh config/server.properties
```

### Use Cases

 **Collecting real time sampled tweets from Twitter and publishing them to our Kafka Broker**

#### Using `producer.py`
Running the script **producer.py** for generating events

#### Using `consumer.py`
Running the script **consumer.py** to consume the events published by the producer.

![SentCosumer](https://user-images.githubusercontent.com/59594174/109211939-ecf41000-777c-11eb-9718-8b9cea41d660.png)

#### Using `twitter-stream.py`
Using the **twitter-stream.py** script to  fetch tweets from Twitter's API in real-time.

Entering our **bearer token** in the twitter.py script under the **BEARER_TOKEN** parameter.

**Tweets are published to the Kafka Broker.**

On running **consumer.py** again, we can see all the published events that are collected by the consumer.

![Tweets](https://user-images.githubusercontent.com/59594174/109211449-3f80fc80-777c-11eb-9811-7545aa019ba4.png)




