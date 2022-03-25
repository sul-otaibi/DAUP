import pandas as pd
import matplotlib.pyplot as plt

columns_name = ['A', 'RTT (ms)', 'B', 'C', 'Download Rate (Mbit/s)', 'D', 'E', 'Upload Rate (Mbit/s)', 'F', 'Date']
with open('Data/rpi_data_long.csv', 'r') as f:
    dataFrame = pd.read_csv(f, names=columns_name)

dataFrame.drop(['A', 'B', 'C', 'D', 'E', 'F'], axis=1, inplace=True)
dataFrame = dataFrame.dropna()

dataFrame['Time'] = dataFrame['Date'].apply(lambda x: x[11:16])

dataFrame = dataFrame.reindex(columns = ['Time', 'Download Rate (Mbit/s)', 'Upload Rate (Mbit/s)', ])
dataFrame['Download Rate (Mbit/s)'] = dataFrame['Download Rate (Mbit/s)'].apply(lambda x: float(x))

acceptable_D_rate = 85
acceptable_U_rate = 12

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 20))
time = pd.to_datetime(dataFrame['Time'])

ax1.hist(dataFrame['Download Rate (Mbit/s)'], 25)
ax1.axvline(acceptable_D_rate, color='red', linewidth=1)
ax1.set_title('Download Rate (Mbit/s)')

ax2.hist(dataFrame['Upload Rate (Mbit/s)'], 25)
ax2.axvline(acceptable_U_rate, color='red', linewidth=1)
ax2.set_title('Upload Rate (Mbit/s)')

plt.show()