import json
import ssl
import time
import paho.mqtt.client as mqtt
import uuid

# Set the certificate and private key paths
#cert_path = "f947ef19df189289aac822ed2a34e98a5f9ef342409bc78aca33f46fc891c774-certificate.pem.crt"
#key_path = "f947ef19df189289aac822ed2a34e98a5f9ef342409bc78aca33f46fc891c774-private.pem.key"


cert_path = "client.crt"
key_path = "client.key"
ca_path = "rootCA.crt"

certificateId = "c245b2956e0de0501504ae4b3b29d427884322d13c5f0e23fe38ea1a8b8c8562"
# Set the AWS IoT endpoint, client ID, and topic to publish to
iot_endpoint = "a3tjhwbszeevie-ats.iot.us-east-1.amazonaws.com"
client_id = str(uuid.uuid4())
#topic = f"$aws/events/certificates/registered/{certificateId}"
topic = 'iot/thermostat/'
timestamp = ""
# Define the MQTT message payload and QoS level
message = {
"certificateId": certificateId,
"caCertificateId": certificateId,
"timestamp": timestamp,
"certificateStatus": "PENDING_ACTIVATION",
"awsAccountId": "awsAccountId",
"certificateRegistrationTimestamp": "certificateRegistrationTimestamp"
}
qos = 1

# Set up the MQTT client
client = mqtt.Client(client_id=client_id, clean_session=True, protocol=mqtt.MQTTv311)

# Configure the TLS connection
context = ssl.create_default_context()
# Load the certificate and private key into the SSL context
context.load_cert_chain(certfile=cert_path, keyfile=key_path)
client.tls_set_context(context)
# Connect to AWS IoT Core
client.connect(iot_endpoint, port=8883)
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






