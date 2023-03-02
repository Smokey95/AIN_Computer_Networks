import os
import matplotlib.pyplot as plt

avg_32 = 33
avg_64 = 32
avg_128 = 35
avg_256 = 36
avg_512 = 33

x = [32, 64, 128, 256, 512]
y = [avg_32, avg_64, avg_128, avg_256, avg_512]

plt.plot(x, y, label = "Average ping time")
plt.xlabel('Packet size (bytes)')
plt.ylabel('Average ping time (ms)')
plt.title('Average ping time for different packet sizes')
plt.legend()
plt.show()