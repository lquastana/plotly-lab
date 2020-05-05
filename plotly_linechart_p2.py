import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/nst-est2017-alldata.csv')
filter_division = df['DIVISION'] == '1'

df_division = df[filter_division]
df_division.set_index('NAME',inplace=True)

filter_pop_col = [col for col in df_division.columns if col.startswith('POP')]

df_division = df_division[filter_pop_col]

print(df_division)

data = [
    go.Scatter(
        x=df_division.columns,
        y=df_division.loc[name],
        mode='lines',
        name=name) for name in df_division.index]

pyo.plot(data)
