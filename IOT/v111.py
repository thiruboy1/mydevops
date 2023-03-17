import paho.mqtt.client as mqtt
import ssl
import json
import uuid
import time


# Configure client ID, endpoint, and port
client_id = str(uuid.uuid4())
endpoint = "a3tjhwbszeevie-ats.iot.us-east-1.amazonaws.com"
port = 8883

# Configure topic and message
topic = "iot/thermostat/"
message = {"key": "value"}

# Configure TLS connection parameters




cert_path = "client.crt"
key_path = "client.key"
ca_path = "rootCA.crt"




qos=1

# Define MQTT client callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")

# Configure MQTT client
client = mqtt.Client(client_id=client_id, clean_session=True, protocol=mqtt.MQTTv311)

# Configure the TLS connection
context = ssl.create_default_context()

# Load the certificate and private key into the SSL context
context.load_cert_chain(certfile=cert_path, keyfile=key_path)
client.tls_set_context(context=context)
#tls_context.load_verify_locations(cafile=ca_path)



client.on_connect = on_connect
client.on_publish = on_publish




# Connect to AWS IoT Core endpoint
client.connect(endpoint, port=port)

# Start the MQTT client loop
client.loop_start()

# Publish the MQTT message
(result, mid) = client.publish(topic, json.dumps(message), qos)
if result == mqtt.MQTT_ERR_SUCCESS:
    print(f"Message published successfully with message ID {mid}")
else:
    print(f"Message publish failed with result code {result}")

# Wait for the message to be sent
time.sleep(1)

# Disconnect from AWS IoT Core
client.disconnect()
