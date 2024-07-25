import dash_nivo as dn
from dash import Dash, html, dcc, Input, Output, State
import json

app = Dash(__name__)

# Load the data from the JSON file
with open('test_data.txt', 'r') as file:
    data = json.load(file)

app.layout = html.Div([
    dn.ResponsiveCircle(
        id='circle-packing',
        data=data,
    ),
    html.Div(id='zoom-info')
])


@app.callback(
    Output('zoom-info', 'children'),
    Input('circle-packing', 'zoomedId')
)
def display_zoom_info(zoomedId):
    if zoomedId:
        return f"Zoomed to: {zoomedId}"
    return "No zoom applied"

if __name__ == '__main__':
    app.run_server(debug=True, port="2321")
