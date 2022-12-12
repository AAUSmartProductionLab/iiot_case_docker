import paho.mqtt.client as mqtt
import mariadb
import sys

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscripte ions will be renewed.
    client.subscribe("test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    print(msg.topic+" "+ str(msg.payload, "utf-8"))
    #cur.execute('INSERT {0} INTO testTable')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mosquitto", 1883, 60) #192.168.1.127

try:
    conn = mariadb.connect(
        user="root",
        password="robotlab",
        host="mariadb",
        port=3306,
        database="iiot_case"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
cur = conn.cursor()

cur.execute("SELECT * FROM users")

for user in cur:
    print(user[0])


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()