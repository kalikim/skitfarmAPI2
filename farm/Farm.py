from flask_restful import Resource
from flask import jsonify, request



import paho.mqtt.client as mqtt #import the client1
import time

class skitfarmPub(Resource):
    def get(self):
        broker_address = "broker.hivemq.com"

        # broker_address="iot.eclipse.org"

        def on_message(client, userdata, message):
            time.sleep(1)
            print("received message =", str(message.payload.decode("utf-8")))

        print("creating new instance")
        client = mqtt.Client("P1")  # create new instance
        print("connecting to broker")
        client.connect(broker_address)  # connect to broker
        print("Subscribing to topic", "code/test")
        client.subscribe("code/test")
        print("Publishing message to topic", "code/test")
        client.on_message = on_message
        client.loop_start()

        while (1):
            client.publish("code/test", "This is the Message @87654")
            print("Send smth")
            client.subscribe("code/test")
            time.sleep(1)

class skitfarmSub(Resource):
    def get(self):
        broker_address = "broker.hivemq.com"

        # broker_address="iot.eclipse.org"

        def on_message(client, userdata, message):
            time.sleep(1)
            print("received message =", str(message.payload.decode("utf-8")))

        print("creating new instance")
        client = mqtt.Client("P1")  # create new instance
        print("connecting to broker")
        client.connect(broker_address)  # connect to broker
        print("Subscribing to topic", "mellowtest/1")
        client.subscribe("mellowtest/1")
        print("Publishing message to topic", "mellowtest/1")
        client.on_message = on_message
        client.loop_start()
        print(client.subscribe("mellowtest/1"))


        return jsonify(client.subscribe("mellowtest/1"))






