import pandas as pd
import matplotlib.pyplot as plt

columns_name = ['A', 'RTT (ms)', 'B', 'C', 'Download Rate (Mbit/s)', 'D', 'E', 'Upload Rate (Mbit/s)', 'F', 'Date']
with open('Data/rpi_data_long.csv', 'r') as f:
    dataFrame = pd.read_csv(f, names=columns_name)

dataFrame.drop(['A', 'B', 'C', 'D', 'E', 'F'], axis = 1, inplace = True)
dataFrame = dataFrame.dropna()

dataFrame['Time'] = dataFrame['Date'].apply(lambda x: x[11:16])

dataFrame = dataFrame.reindex(columns = ['Time', 'Download Rate (Mbit/s)', 'Upload Rate (Mbit/s)', ])
dataFrame['Download Rate (Mbit/s)'] = dataFrame['Download Rate (Mbit/s)'].apply(lambda x: float(x))

downlod_mean = dataFrame['Download Rate (Mbit/s)'].mean()
downlod_std = dataFrame['Download Rate (Mbit/s)'].std()

upload_mean = dataFrame['Upload Rate (Mbit/s)'].mean()
upload_std = dataFrame['Upload Rate (Mbit/s)'].std()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
time = pd.to_datetime(dataFrame['Time'])

ax1.plot(time, dataFrame['Download Rate (Mbit/s)'], '-r', linewidth=1, label='Download Rate (Mbit/s)')
ax1.plot(time, [downlod_mean] * len(time), '-g', linewidth=3, label='Download Rate (Mbit/s) Mean')
ax1.set_title('Download Rate (Mbit/s)')
ax1.legend()
ax1.grid()

ax2.plot(time, dataFrame['Upload Rate (Mbit/s)'], '-r', linewidth=1, label='Upload Rate (Mbit/s)')
ax2.plot(time, [upload_mean] * len(time), '-g', linewidth=3, label='Upload Rate (Mbit/s) Mean')
ax2.set_title('Upload Rate (Mbit/s)')
ax2.legend()
ax2.grid()

plt.show()