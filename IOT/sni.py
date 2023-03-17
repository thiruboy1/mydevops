import ssl
import time
import paho.mqtt.client as mqtt
import json
import uuid
# Configure the connection parameters
awshost = "a3tjhwbszeevie-ats.iot.us-east-1.amazonaws.com"
awsport = 8883
clientId =  str(uuid.uuid4())
topic = f"iot/just-in-time-registration/request/"
certificatePath = "client.crt"
privateKeyPath = "client.key"
caPath = None  # No CA certificate is required for SNI-based JIT registration
sniHostname = "a3tjhwbszeevie-ats.iot.us-east-1.amazonaws.com"

# Define the callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Set up the MQTT client
client = mqtt.Client(clientId)


# Configure the TLS SNI extension
context = ssl.create_default_context()
context.set_servername_callback(lambda _: sniHostname)

client.on_connect = on_connect
client.on_message = on_message

# Load the certificate and private key into the SSL context
context.load_cert_chain(certfile=certificatePath, keyfile=privateKeyPath)
client.tls_set_context(context)



# Connect to AWS IoT Core and start the MQTT loop
client.connect(awshost, awsport, keepalive=60)

# Start the MQTT client loop
client.loop_start()

# Publish the MQTT message
message = {"hello": "world"}
client.publish(topic, json.dumps(message))
print("done")
# Wait for a few seconds and then disconnect
time.sleep(5)
client.loop_stop()
client.disconnect()
