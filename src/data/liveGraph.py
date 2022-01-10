import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)


def animate(i):
    graph_data=pd.read_csv('Voltage.csv')
    print((graph_data["Channel5"])[0])
    c5=graph_data["Channel5"]
    xs = []
    for value in c5:
        if(value):
           print(value)
           #xs.append(value)

    print(xs)
    ax1.clear()
    ax1.cla()
    ax1.plot(xs)


ani = animation.FuncAnimation(fig, animate,interval=100)
plt.tight_layout()
plt.show()
