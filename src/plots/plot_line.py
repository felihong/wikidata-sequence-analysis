import plotly
plotly.tools.set_credentials_file(username='Felihong', api_key='YZpXs9wn4DSmnDD8acmW')
import plotly.io as pio
import plotly.graph_objs as go

trace = go.Scatter(
    x = [0, 1, 2, 3, 4, 5],
    y = [0, 0.0082, 0.0522, 0.0672, 0.0772, 0.08],
    marker=dict( color='#35a1ea')
)

data = [trace]

layout = go.Layout(
    xaxis = go.layout.XAxis(
        tickmode = 'array',
        tickvals = [0, 1, 2, 3, 4],
        ticktext = ['E', 'D', 'C', 'B', 'A'],
        showgrid = False
    ),
    yaxis = go.layout.YAxis(
        showgrid = True
    )
)

fig = go.Figure(
    data = data,
    layout = layout
)

pio.write_image(fig, 'js_line.pdf')


