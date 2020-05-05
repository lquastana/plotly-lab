import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/2010YumaAZ.csv')

data = []

for day in df['DAY'].unique() :
    filter_day = df['DAY'] == day
    trace = go.Scatter(
        x=df['LST_TIME'],
        y=df[filter_day]['T_HR_AVG'],
        mode='lines',
        name=day)
    data.append(trace)


pyo.plot(data)
