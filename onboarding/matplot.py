'''
TODO
- Graph all the data. This can be all the same plot, or four separate plots
    Use Matplotlib, please!
- Be careful of data points that don't exist
- Will require reading from CSV, can experiment with pandas
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("test_data.csv")

# Replace Blank values with DataFrame.replace() methods.
df = df.replace(' ', np.nan)                   # to get rid of empty values
nan_values = df[df.isna().any(axis=1)] 
col_labels = {'0':'First',
             '0.1':'Second',
             '0.2':'Third',
             '0.3':'Fourth',
              "1": "Fifth",
             }
df.rename(columns=col_labels,inplace=True)
print("Line graph: ")
plt.plot(df["First"], df["Second"])
plt.show()
print("Line graph: ")
plt.plot(df["First"], df["Third"])
plt.show()
print("Line graph: ")
plt.plot(df["First"], df["Fourth"])
plt.show()
print("Line graph: ")
plt.plot(df["First"], df["Fourth"])
plt.show()


