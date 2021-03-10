# %%

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

dataset = pd.read_csv('RRCA_baseflow.csv')

# %%

sns.scatterplot(data=dataset, x='Date', y='Observed')
plt.show()
# %%
