from paho.mqtt import client as mqtt_client
import csv
import numpy as np
import pandas as pd



broker = '192.168.0.101'
port = 1883
topic = "Data"
client_id = ''
username = 'Reinstated'
password = 'whatthehell'
myFile = open('Voltage.csv', 'w',newline="")
writer = csv.writer(myFile)
writer.writerow(['Channel1','Channel2','Channel3','Channel4','Channel5','Channel6', 'Channel7','Channel8',])
x1 = np.array([])
x2 = np.array([])
x3 = np.array([])
x4 = np.array([])
x5 = []
x6 = []
x7 = np.array([])
#x0=[]

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

        channelvalue = pd.DataFrame()


        rawdata=int((msg.payload))
        #print(rawdata)


        x5.append((int(rawdata) & 0x0FFF))
        x6.append((int(rawdata) >> 12))

      #  tmp = [(int(rawdata) & 0x0FFF), (int(rawdata) >> 12)]
       # writer.writerow(tmp)

        channel = int(rawdata) >> 12
        if ((int(rawdata) & 0x0FFF) < 4097):
            if (channel == 0):
                tmp = [(int(rawdata) & 0x0FFF)]
                writer.writerow(tmp)
            elif (channel == 1):
                tmp = ['',(int(rawdata) & 0x0FFF)]
                writer.writerow(tmp)
            elif (channel == 2):
                 tmp = ['','',(int(rawdata) & 0x0FFF)]
                 writer.writerow(tmp)
            elif (channel == 3):
                tmp = ['','','',(int(rawdata) & 0x0FFF)]
                writer.writerow(tmp)
            elif (channel == 4):
                tmp = ['','','','',(int(rawdata) & 0x0FFF)]
                writer.writerow(tmp)
            elif (channel == 5):
                tmp = ['','','','','',(int(rawdata) & 0x0FFF)]
                writer.writerow(tmp)
            elif (channel == 6):
                tmp = ['','','','','','',(int(rawdata) & 0x0FFF)]
                writer.writerow(tmp)
            elif (channel == 7):
                tmp = ['','','','','','','',(int(rawdata) & 0x0FFF)]
                writer.writerow(tmp)

        #myFile.close()

        fs = open('Voltage.csv')
        reader = csv.reader(fs)
        lines = len(list(reader))

        print(lines)

        #channelvalue.append({'Channel5': (int(rawdata) & 0x0FFF)}, ignore_index=True)
        #print("len:", channelvalue)

   # cities['new'] = pd.Series([x0[i] for x in range(len(x2))])
#create NumPy array for 'blocks'
#blocks = np.array([2, 3, 1, 0, 2, 7, 8, 2])

        #channelvalue['Channel5'] = x5
        #channelvalue['Channel6'] = x6
        #fs = open('Voltage.csv', 'w')
        #channelvalue.to_csv(fs,index=None)
        #fs.close()
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





