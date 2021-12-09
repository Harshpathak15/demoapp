from matplotlib import colors
import matplotlib.pyplot as plt
import pandas as pd
with open('iris.csv') as f:
    data = pd.read_csv(f)

sl=data['sepal.length']
sw=data['sepal.width']
pl=data['petal.length']
pw=data['petal.width']
ax=plt.axes(projection='3d')
ax.scatter(sl,sw,label='Sepal',c='Red')
ax.scatter(pl,pw,label='PeTal',c='black')
plt.legend
plt.show()
