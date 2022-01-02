import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./data/spreadspoke_scores.csv')

print(df)

new_df = df.dropna()
print(new_df)

# print(new_df.head())

print("column names:", list(new_df.columns))


print("Now time for a plot")
df.plot(kind = 'scatter', x = 'weather_temperature', y = 'weather_wind_mph')

plt.show()

# plt.clf()
# heatmap, xedges, yedges = np.histogram2d(new_df["weather_temperature"], new_df["weather_wind_mph"], bins=8)
# extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
# plt.imshow(heatmap.T, extent=extent, origin='lower')
# plt.show()
