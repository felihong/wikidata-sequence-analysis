import plotly

plotly.tools.set_credentials_file(username='Felihong', api_key='YZpXs9wn4DSmnDD8acmW')
import plotly.io as pio

fig = {
    "data": [
        {
            "values": [129, 95, 68, 59, 35, 34],
            "labels": [
                "Geography and Places",
                "Objective Reality",
                "Human and Self",
                "Life and Society",
                "Science and Technology",
                "Culture, Art and History"
            ],
            "domain": {"column": 0},
            "hoverinfo": "label+percent+name",
            "textfont": {'color': '#FFFFFF'},
            "hole": .45,
            "type": "pie",
            "marker": {
                "colors": ['#35a1ea', '#ffce55', '#4bc0bf', '#9966fe', '#fe9e40', '#ff6383']
            }
        }],
    "layout": {
        "annotations": [
            {
                "font":
                 {
                     "size": 50
                 },
                "showarrow": False,
                "text": " ",
                "x": 0.2,
                "y": 0.2
            }
        ],
        "legend" : dict(orientation="h")
    }
}
pio.write_image(fig, 'pic_vertical.pdf')
