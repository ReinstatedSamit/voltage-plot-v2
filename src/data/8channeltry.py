import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import os.path


myFile = open('V123.csv', 'r')
colname={'Channel5':[]}
#x0=[]
x0=np.array([])
x1=np.array([])
x2=np.array([])
x3=np.array([])
x4=np.array([])
x5=np.array([])
x6=np.array([])
x7=np.array([])

for rows in myFile:
    if (rows != '\n'):
        rawdata = int(rows) >> 12
        print(rawdata)
        if ((int(rows) & 0x0FFF) < 4097):
            if (rawdata == 0):
                #x0.append((int(rows) & 0x0FFF))
                x0 = np.append(x0, (int(rows) & 0x0FFF))
                print("Channel0:", (int(rows) & 0x0FFF))
            elif (rawdata == 1):
                x1 = np.append(x1, (int(rows) & 0x0FFF))
                print("Channel1:", (int(rows) & 0x0FFF))
            elif (rawdata == 2):
                x2 = np.append(x2, (int(rows) & 0x0FFF))
                print("Channel2:", (int(rows) & 0x0FFF))
            elif (rawdata == 3):
                x3 = np.append(x3, (int(rows) & 0x0FFF))
                print("Channel3:", (int(rows) & 0x0FFF))
            elif (rawdata == 4):
                x4 = np.append(x4, (int(rows) & 0x0FFF))
                print("Channel4:", (int(rows) & 0x0FFF))
            elif (rawdata == 5):
                x5 = np.append(x5, (int(rows) & 0x0FFF))
                print("Channel5:", (int(rows) & 0x0FFF))
            elif (rawdata == 6):
                x6 = np.append(x6, (int(rows) & 0x0FFF))
                print("Channel6:", (int(rows) & 0x0FFF))
            elif (rawdata == 7):
                x7 = np.append(x7, (int(rows) & 0x0FFF))
                print("Channel7:", (int(rows) & 0x0FFF))




print("Len of Chennel0",len(x0))
print("Len of Chennel1",len(x1))
print("Len of Chennel2",len(x2))
print("Len of Chennel3",len(x3))
print("Len of Chennel4",len(x4))
print("Len of Chennel5",len(x5))
print("Len of Chennel6",len(x6))
print("Len of Chennel7",len(x7))

print("Chennel0",(x0))
print("Chennel1",(x1))
print("Chennel2",(x2))
print("Chennel3",(x3))
print("Chennel4",(x4))
print("Chennel5",(x5))
print("Chennel6",(x6))
print("Chennel7",(x7))

print("Chennel7 type",type(x0))
max_num=[len(x0),len(x1),len(x2),len(x3),len(x4),len(x5),len(x6),len(x7)]
max=max(max_num)
x0=np.pad(x0,(0,(max-len(x0))),'constant',constant_values=(0,0))
x1=np.pad(x1,(0,(max-len(x1))),'constant')
x2=np.pad(x2,(0,(max-len(x2))),'constant')
x3=np.pad(x3,(0,(max-len(x3))),'constant')
x4=np.pad(x4,(0,(max-len(x4))),'constant')
x5=np.pad(x5,(0,(max-len(x5))),'constant')
x6=np.pad(x6,(0,(max-len(x6))),'constant',constant_values=(0,0))
x7=np.pad(x7,(0,(max-len(x7))),'constant')

print("Len of Chennel0",len(x0))
print("Len of Chennel1",len(x1))
print("Len of Chennel2",len(x2))
print("Len of Chennel3",len(x3))
print("Len of Chennel4",len(x4))
print("Len of Chennel5",len(x5))
print("Len of Chennel6",len(x6))
print("Len of Chennel7",len(x7))

#cities = pd.DataFrame([[x0[i], x1,x2]], columns=['Channel0', 'Channel1','Channel2'])
#for i in range(0,400):
channelvalue = pd.DataFrame(index=range(0,max))
   # cities['new'] = pd.Series([x0[i] for x in range(len(x2))])
#create NumPy array for 'blocks'
#blocks = np.array([2, 3, 1, 0, 2, 7, 8, 2])

#add 'blocks' array as new column in DataFrame
channelvalue['Channel0'] = x0.tolist()
channelvalue['Channel1'] = x1.tolist()
channelvalue['Channel2'] = x2.tolist()
channelvalue['Channel3'] = x3.tolist()
channelvalue['Channel4'] = x4.tolist()
channelvalue['Channel5'] = x5.tolist()
channelvalue['Channel6'] = x6.tolist()
channelvalue['Channel7'] = x7.tolist()
#
channelvalue.to_csv('Voltage.csv')


plt.plot(x0)
plt.plot(x1)
plt.plot(x2)
plt.plot(x3)
plt.plot(x4)
plt.plot(x5)
plt.plot(x6)
plt.plot(x7)
plt.show()
