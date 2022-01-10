from paho.mqtt import client as mqtt_client
import csv
import numpy as np



broker = '192.168.0.131'
port = 1883
topic = "Data"
client_id = ''
username = 'Reinstated'
password = 'whatthehell'
#myFile = open('Constantv.csv', 'w')
x=[]

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
       # D = float(msg.payload.decode())
        #x.append((msg.payload.decode()))
        a=int((msg.payload))
        x.append(a)
        print(type(int(msg.payload)))
        y=np.transpose(x)
        print(int(msg.payload))
        print(x)
        print(y)
        myFile = open('V123.csv', 'w')
        with myFile:
            writer = csv.writer(myFile,delimiter='\n')
            writer.writerow(y)

       # print(len(x))
      #  print(x)






    client.subscribe(topic)
    client.on_message = on_message



def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()



if __name__ == '__main__':

    run()