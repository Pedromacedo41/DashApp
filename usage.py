from gridlayout import GridLayout
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

layout = [{"i": 'a', "x": 0, "y": 0, "w": 4, "h": 4},
          {"i": 'b', "x": 1, "y": 0, "w": 4, "h": 4, "minW": 2, "maxW": 4}]


app.layout = html.Div([
    GridLayout(
        id='inputt',
        layout= layout,
        children=[
            html.Div("test1"),
            html.Div("test2")
        ]
    ),
    html.Div(id='output')
])


if __name__ == '__main__':
    #print([html.Div(**{"data-grid": a, "key": a["i"], "children": [html.P(a["i"])]}) for a in layout])
    app.run_server(debug=True)
