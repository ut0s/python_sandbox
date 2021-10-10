#!/usr/bin/env python3

import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

df = px.data.stocks()
df['GOOG-AAPL'] = df['GOOG'] - df['AAPL']
print(df.info())

fig = px.line(df, x='date', y=df.columns[1:6], title="6 company stocks plot", hover_data=["date", "GOOG-AAPL"])

# fig.update_xaxes(
#   dtick="M1",
#   tickformat="%b\n%Y")

fig.update_layout(template=go.layout.Template())
fig.update_layout(showlegend=True)  # 凡例を強制的に表示（デフォルトでは複数系列あると表示）
fig.update_traces(mode="markers+lines")
fig.update_layout(hovermode='x unified')

fig.show()


# ref
# https://cafe-mickey.com/python/plotly-layout-2/
