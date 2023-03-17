import paho.mqtt.client as mqtt
import ssl
import uuid
import json
import time

endpoint = "a3tjhwbszeevie-ats.iot.us-east-1.amazonaws.com"
cert_path = "client_3_newca.crt"
key_path = "client_3_newca.key"
ca_path = "rootCA.crt"

awsport = 8883
clientId =  str(uuid.uuid4())
#topic = f"iot/just-in-time-registration/request/"

topic = 'iot/thermostat/'
qos = 1

# Define MQTT client callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published")


def Register():
    topic = f"iot/just-in-time-registration/request/"
    # Configure MQTT client
    client = mqtt.Client(client_id=clientId, protocol=mqtt.MQTTv311)

   # Configure the TLS connection
    ssl_context = ssl.create_default_context()


    ssl_context.set_alpn_protocols(["x-amzn-mqtt-ca"])

    # Load the certificate and private key into the SSL context
    ssl_context.load_cert_chain(certfile=cert_path, keyfile=key_path)

    # Configure SNI for JITR
    ssl_context.server_hostname = endpoint
    client.tls_set_context(context=ssl_context)

    # Connect to AWS IoT Core
    client.connect(endpoint, port=8883)

    # Publish a message to a topic

    payload = {"hello": "world"}
    print(client.publish(topic,  json.dumps(payload)))

    # Disconnect from AWS IoT Core
    client.disconnect()

#Register(topic)

def PublishMqttMessage(message,topic):    
    # Configure MQTT client
    client = mqtt.Client(client_id=clientId, clean_session=True, protocol=mqtt.MQTTv311)
    # Configure the TLS connection
    context = ssl.create_default_context()
    # Load the certificate and private key into the SSL context
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)
    client.tls_set_context(context=context)
    #tls_context.load_verify_locations(cafile=ca_path)
    client.on_connect = on_connect
    client.on_publish = on_publish
    # Connect to AWS IoT Core endpoint
    client.connect(endpoint, port=awsport)
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

topic = "iot/thermostat/"
message = {"DeviceID": "3","temprature": "21"}
#Register()
PublishMqttMessage(message,topic)