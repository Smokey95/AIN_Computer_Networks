# import OS module
import os
import matplotlib.pyplot as plt

curr_dirname = os.path.dirname(__file__)
print(curr_dirname)

# Get the list of all files and directories
data_dir = curr_dirname[:-3] + "data"
print(data_dir)
dir_list = os.listdir(data_dir)
print("Files and directories in '", data_dir, "' :")
# prints all files
# print(dir_list)

time_htwg = []
time_berlin = []
time_ohio = []
time_au = []


print("--------------------")

# Read the data (very ugly code)

# get time from australia file
with open(data_dir + '\\' + dir_list[0], encoding='utf-8') as f:
    for line in f:
      time_au.append(line.split("time=")[1].split("ms")[0])

# get time from berlin file
with open(data_dir + '\\' + dir_list[1], encoding='utf-8') as f:
    for line in f:
      time_berlin.append(line.split("time=")[1].split("ms")[0])

# gets time data from htwg file
with open(data_dir + '\\' + dir_list[2], encoding='utf-8') as f:
    for line in f:
      time_htwg.append(line.split("time=")[1].split("ms")[0])
      
# gets time data from ohio file
with open(data_dir + '\\' + dir_list[3], encoding='utf-8') as f:
    for line in f:
      time_ohio.append(line.split("time=")[1].split("ms")[0])
      
print(time_htwg)
print(time_berlin)
print(time_au)
print(time_ohio)

x = [i for i in range(1, len(time_htwg) + 1)]

plt.plot(x, time_htwg, label = "HTWG Konstanz")
plt.plot(x, time_berlin, label = "HTW Berlin")
plt.plot(x, time_ohio, label = "Ohio State University")
plt.plot(x, time_au, label = "Australia University")

plt.xlabel('Number of pings')
#plt.ylabel('Time (ms)')
plt.title('Ping time')
plt.legend()
plt.show()