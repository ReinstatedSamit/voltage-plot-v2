channelvalue['Channel1'] = x1.tolist()
        channelvalue['Channel2'] = x2.tolist()
        channelvalue['Channel3'] = x3.tolist()
        channelvalue['Channel4'] = x4.tolist()
        channelvalue['Channel5'] = x5.tolist()
        channelvalue['Channel6'] = x6.tolist()
        channelvalue['Channel7'] = x7.tolist()
        channelvalue['Channel8'] = x8.tolist()
channel=int(rawdata) >> 12
        if ((int(rawdata) & 0x0FFF) < 4097):
            if (channel == 0):
                x1 = np.append(x1, (int(rawdata) & 0x0FFF))
                channelvalue = channelvalue.append({'Channel1':(int(rawdata) & 0x0FFF)}, ignore_index=True)
                print("Channel1:", (int(rawdata) & 0x0FFF))
            elif (channel == 1):
                x2 = np.append(x1, (int(rawdata) & 0x0FFF))
                channelvalue = channelvalue.append({'Channel2': (int(rawdata) & 0x0FFF)}, ignore_index=True)
                print("Channel2:", (int(rawdata) & 0x0FFF))
            elif (channel == 2):
                x3 = np.append(x3, (int(rawdata) & 0x0FFF))
                channelvalue = channelvalue.append({'Channel3': (int(rawdata) & 0x0FFF)}, ignore_index=True)
                print("Channel3:", (int(rawdata) & 0x0FFF))
            elif (channel == 3):
                x4 = np.append(x4, (int(rawdata) & 0x0FFF))
                channelvalue = channelvalue.append({'Channel4': (int(rawdata) & 0x0FFF)}, ignore_index=True)
                print("Channel4:", (int(rawdata) & 0x0FFF))
            elif (channel == 4):
                 x5 = np.append(x5, (int(rawdata) & 0x0FFF))
                 channelvalue = channelvalue.append({'Channel5': (int(rawdata) & 0x0FFF)}, ignore_index=True)
                 print("Channel5:", (int(rawdata) & 0x0FFF))
            elif (channel == 5):
                x6 = np.append(x6, (int(rawdata) & 0x0FFF))
                channelvalue = channelvalue.append({'Channel6': (int(rawdata) & 0x0FFF)}, ignore_index=True)
                print("Channel6:", (int(rawdata) & 0x0FFF))
            elif (channel == 6):
                x7 = np.append(x7, (int(rawdata) & 0x0FFF))
                channelvalue = channelvalue.append({'Channel7': (int(rawdata) & 0x0FFF)}, ignore_index=True)
                print("Channel7:", (int(rawdata) & 0x0FFF))
            elif (channel == 7):
                x8 = np.append(x8, (int(rawdata) & 0x0FFF))
                channelvalue = channelvalue.append({'Channel8': (int(rawdata) & 0x0FFF)}, ignore_index=True)
                print("Channel8:", (int(rawdata) & 0x0FFF))
