

import pandas as pd
import csv

df = pd.read_csv("data2.csv")

import plotly.figure_factory as ff

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Rating"], show_hist = True)
fig.show()