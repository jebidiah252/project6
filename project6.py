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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from statistics import mean 
import itertools

def test_combinations(month):
    points = dataset[dataset['Month'] == month]
    points = points.groupby('Segment_id', as_index=False).mean()
    # train_set, test_set = train_test_split(points)
    feature_cols = ['Evapotranspiration', 'Precipitation', 'Irrigation_pumping']
    for i in range(1, len(feature_cols) + 1):
        for subset in itertools.combinations(feature_cols, i):
            subset = list(subset)
            print(subset)
            X = points[subset]
            y = points['Observed']
            lm = LinearRegression()
            lm.fit(X, y)
            print(lm.score(X, y))

def test():
    # train_set, test_set = train_test_split(points)
    feature_cols = ['Evapotranspiration', 'Precipitation', 'Irrigation_pumping']
    for i in range(1, len(feature_cols) + 1):
        for subset in itertools.combinations(feature_cols, i):
            scores = []
            for month in range(1, 13):
                points = dataset[dataset['Month'] == month]
                points = points.groupby('Segment_id', as_index=False).mean()
                subset = list(subset)
                X = points[subset]
                y = points['Observed']
                lm = LinearRegression()
                lm.fit(X, y)
                scores.append(lm.score(X, y))
            print(subset)
            print(mean(scores))
            print()
            # X_new = pd.DataFrame({column: [50, 55, 60]})
            # predictions = lm.predict(test_set[subset].values)
            # iterator = [row for row in train_set.iterrows()]
            # differences = []
            # for i in range(len(predictions)):
            #     differences.append(iterator[i][1]['Observed'] - predictions[i])
            # print(month)
            # print(mean(differences))
            # print()



def plot_observed_vs_segment(month):
    points = dataset[dataset['Month'] == month]
    points = points.groupby('Segment_id', as_index=False).mean()
    for column in points.columns:
        if column not in ['Observed', 'Month', 'Date', 'x', 'y', 'Segment_id']:
            # sns.scatterplot(data=points, x=column, y='Observed')
            # plt.show()
            test(points, column)

for i in range(1, 12 + 1):
    test_combinations(i)

test()

# %%
