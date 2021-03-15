# %%
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import datetime

dataset = pd.read_csv('RRCA_baseflow.csv')
dataset.columns

# %%
sns.scatterplot(data=dataset, x='Segment_id', y='Observed')
plt.show()

# first day starts at December 3rd, 1945 or 1946
sns.scatterplot(data=dataset, x='Date', y='Observed')
plt.show()

# %%
cmap = sns.cubehelix_palette(as_cmap=True)

f, ax = plt.subplots()
print(dataset.groupby(['x','y']).mean())
points = ax.scatter(dataset['x'], dataset['y'], c=dataset['Observed'], cmap=cmap)
f.colorbar(points)
# %%
months = []
for index, row in dataset.iterrows():
    new_date = datetime.datetime(1, 1, 1, 0, 0) + datetime.timedelta(row['Date'] - 365)
    months.append(int(new_date.strftime('%m')))
dataset['Month'] = months
sns.scatterplot(data=dataset, x='Month', y='Observed')
plt.show()

# %%
january_points = dataset[dataset['Month'] == 1]
january_points = january_points.groupby('Segment_id', as_index=False)['Observed'].mean()
sns.scatterplot(data=january_points, x='Segment_id', y='Observed')
plt.show()
# %%
def plot_observed_vs_segment(month):
    points = dataset[dataset['Month'] == month]
    points = points.groupby('Segment_id', as_index=False).mean()
    for column in points.columns:
        if column not in ['Observed', 'Month']:
            sns.scatterplot(data=points, x=column, y='Observed')
            plt.show()

for i in range(1, 12 + 1):
    plot_observed_vs_segment(i)

# %%
