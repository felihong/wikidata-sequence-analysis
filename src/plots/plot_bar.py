import plotly
plotly.tools.set_credentials_file(username='Felihong', api_key='YZpXs9wn4DSmnDD8acmW')
import plotly.io as pio
import plotly.graph_objs as go

trace_js = go.Bar(
    x= ['E', 'D', 'C', 'B', 'A'],
    y= [0.0082, 0.0440, 0.0158, 0.0100, 0.0028],
    text= [0.008, 0.044, 0.016, 0.010, 0.003],
    textposition = 'auto',
    marker=dict(
        color=['#ffce55','#ffce55','#ffce55','#ffce55','#ffce55'],
    )
)

data = [trace_js]

layout = go.Layout(
    yaxis = go.layout.YAxis(
        showgrid = False
    )
)

fig = go.Figure(data=data, layout=layout)
pio.write_image(fig, 'js_bar.pdf')