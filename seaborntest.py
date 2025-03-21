import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D


df = sns.load_dataset('planets')
print(df.head())

sns.pairplot(df,hue='mass')
plt.suptitle('Pairplot - Planets Dimensions',y = 2)
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
df_clean = df.dropna()
ax.scatter(df_clean['orbital_period'],df_clean['mass'], df_clean['distance'], c=pd.Categorical(df_clean['mass']).codes, cmap = 'viridis')
ax.set_xlabel('orbital_period')
ax.set_ylabel('mass')
ax.set_zlabel('distance')
plt.title('3D Scatter Plot')
plt.show()
#3D IRIS
# df = sns.load_dataset('Iris')
# sns.pairplot(df,hue='species')
#plt.suptitle('Pairplot - Iris Dimensions',y = 1.02)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# df_clean = df.dropna()
# ax.scatter(df_clean['sepal_length'],df_clean['sepal_width'], df_clean['petal_length'], c=pd.Categorical(df_clean['species']).codes, cmap = 'viridis')
# ax.set_xlabel('sepal_length')
# ax.set_ylabel('sepal_width')
# ax.set_zlabel('petal_length')
# plt.title('3D Scatter Plot')
#3D PENGUINS
# df = sns.load_dataset('penguins')
# sns.pairplot(df,hue='species')
# plt.suptitle('Pairplot - Penguins Dimensions',y = 1.02)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# df_clean = df.dropna()
# ax.scatter(df_clean['bill_length_mm'],df_clean['bill_depth_mm'], df_clean['flipper_length_mm'], c=pd.Categorical(df_clean['species']).codes, cmap = 'viridis')
# ax.set_xlabel('bill_length(mm)')
# ax.set_ylabel('bill_depth(mm)')
# ax.set_zlabel('flipper_length(mm)')

#2D PENGUINS
# sns.scatterplot(df, x = 'sepal_length', y = 'sepal_width', hue='species')
plt.show()