import os
from statistics import mean

import pandas as pd
import matplotlib.pyplot as plt

datasets_loc: str = "../datasets/json_queries/"

datasets: list[pd.DataFrame] = []

for root, _, files in os.walk(datasets_loc):
    for dataset in files:
        path = os.path.join(root, dataset)
        datasets.append(pd.read_json(path, orient="index"))

scores: dict[pd.DatetimeIndex, list[int]] = {}
to_plot: list[float] = []

for df in datasets:
    query = df.columns[0]
    for date in df.index:
        if date not in scores:
            scores[date] = []
        scores[date].append(df[query][date])

for date in scores:
    to_plot.append(mean(scores[date]))

plt.plot(list(scores.keys()), to_plot)
plt.legend(["Frequency of Croatia vacation related searches"])
plt.show()
