# import necessary libraries
import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

# create DataFrame
df1 = pd.read_csv('data1.csv', sep=',')
df2 = pd.read_csv('data2.csv', sep=',')

# combine two DataFrames into one DataFrame with the index as the date column
df = pd.merge(df1, df2)

# create stacked bar chart for monthly temperatures
plot = df.plot(kind='bar', stacked=True, color=['red', 'skyblue', 'green'], x="Date")

# labels for x & y axis
plt.xlabel('Months')
plt.ylabel('Temp ranges in Degree Celsius')

# title of plot
plt.title('Monthly Temperatures in a year')

n = 5
for index, label in enumerate(plot.xaxis.get_ticklabels()):
    if index % n != 0:
        label.set_visible(False)


plt.show()

plot.get_figure().savefig("out.png")
