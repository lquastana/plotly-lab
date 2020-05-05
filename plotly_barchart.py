import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/2018WinterOlympics.csv')

data = []


trace_gold = go.Bar(
    x=df['NOC'],
    y=df['Gold'],
    name='Gold',
    marker={'color':'#FFD700'})

data.append(trace_gold)

trace_silver = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    name='Silver',
    marker={'color':'#9EA0A1'})

data.append(trace_silver)

trace_bronze = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    name='Bronze',
    marker={'color':'#CD7F32'})

data.append(trace_bronze)


pyo.plot(data)
