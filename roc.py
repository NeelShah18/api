import pandas as pd
import scikitplot as skplt
import matplotlib.pyplot as plt

df = pd.read_csv("~/svm/upload.csv")
x = df.X
y = df.Y
skplt.metrics.plot_roc_curve(df.Y, df.X)
plt.show()