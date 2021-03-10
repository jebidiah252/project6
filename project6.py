# %%

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

dataset = pd.read_csv('RRCA_baseflow.csv')

# %%

# first day starts at December 3rd, 1945 or 1946
sns.scatterplot(data=dataset, x='Date', y='Observed')
plt.show()
# %%
