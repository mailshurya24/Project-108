import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("project/ratings.csv")

fig = ff.create_distplot([df["M"].tolist()], ["M"], show_hist = False)
fig.show()