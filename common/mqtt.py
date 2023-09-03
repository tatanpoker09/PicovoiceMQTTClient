import paho.mqtt.client as mqtt


class MqttClient:
    def __init__(self, BROKER_ADDRESS, BROKER_PORT):
        self.client = mqtt.Client()
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.BROKER_ADDRESS = BROKER_ADDRESS
        self.BROKER_PORT = BROKER_PORT

    def connect(self):
        self.client.connect(self.BROKER_ADDRESS, self.BROKER_PORT, 60)


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
