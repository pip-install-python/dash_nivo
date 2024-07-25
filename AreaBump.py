import dash_nivo
from dash import Dash, html, dcc, Input, Output, State
import json

app = Dash(__name__)

# Load the data
data = [
    {
        "id": "JavaScript",
        "data": [
            {"x": 2000, "y": 17},
            {"x": 2001, "y": 28},
            {"x": 2002, "y": 10},
            {"x": 2003, "y": 29},
            {"x": 2004, "y": 13},
            {"x": 2005, "y": 15}
        ]
    },
    {
        "id": "ReasonML",
        "data": [
            {"x": 2000, "y": 27},
            {"x": 2001, "y": 21},
            {"x": 2002, "y": 13},
            {"x": 2003, "y": 14},
            {"x": 2004, "y": 27},
            {"x": 2005, "y": 20}
        ]
    },
    {
        "id": "TypeScript",
        "data": [
            {"x": 2000, "y": 22},
            {"x": 2001, "y": 23},
            {"x": 2002, "y": 20},
            {"x": 2003, "y": 23},
            {"x": 2004, "y": 17},
            {"x": 2005, "y": 13}
        ]
    },
    {
        "id": "Elm",
        "data": [
            {"x": 2000, "y": 26},
            {"x": 2001, "y": 11},
            {"x": 2002, "y": 10},
            {"x": 2003, "y": 12},
            {"x": 2004, "y": 17},
            {"x": 2005, "y": 25}
        ]
    },
    {
        "id": "CoffeeScript",
        "data": [
            {"x": 2000, "y": 22},
            {"x": 2001, "y": 20},
            {"x": 2002, "y": 14},
            {"x": 2003, "y": 28},
            {"x": 2004, "y": 15},
            {"x": 2005, "y": 28}
        ]
    }
]

app.layout = html.Div([
    dash_nivo.AreaBump(
        id='area-bump',
        data=data,
        margin={'top': 40, 'right': 100, 'bottom': 40, 'left': 100},
        spacing=8,
        colors={'scheme': 'nivo'},
        blendMode='multiply',
        defs=[
            {
                'id': 'dots',
                'type': 'patternDots',
                'background': 'inherit',
                'color': '#38bcb2',
                'size': 4,
                'padding': 1,
                'stagger': True
            },
            {
                'id': 'lines',
                'type': 'patternLines',
                'background': 'inherit',
                'color': '#eed312',
                'rotation': -45,
                'lineWidth': 6,
                'spacing': 10
            }
        ],
        fill=[
            {
                'match': {
                    'id': 'CoffeeScript'
                },
                'id': 'dots'
            },
            {
                'match': {
                    'id': 'TypeScript'
                },
                'id': 'lines'
            }
        ],
        startLabel='id',
        endLabel='id',
        axisTop={
            'tickSize': 5,
            'tickPadding': 5,
            'tickRotation': 0,
            'legend': '',
            'legendPosition': 'middle',
            'legendOffset': -36
        },
        axisBottom={
            'tickSize': 5,
            'tickPadding': 5,
            'tickRotation': 0,
            'legend': '',
            'legendPosition': 'middle',
            'legendOffset': 32
        }
    ),
    html.Div(id='click-data')
])

@app.callback(
    Output('click-data', 'children'),
    Input('area-bump', 'clickedPoint')
)
def display_click_data(clickedPoint):
    if clickedPoint is None:
        return 'Click on a point to see its data'
    return f'Clicked point: {json.dumps(clickedPoint, indent=2)}'


if __name__ == '__main__':
    app.run_server(debug=True, port="2321")