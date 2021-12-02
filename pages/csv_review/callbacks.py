# import main app object for callback registration
from app import app 

# import of external libraries
import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State, ALL, MATCH
import dash_html_components as html

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd
import json
import sys, traceback
import io
import re
import dash_ace

# import of internal modules
from utils import make_toast
from pages.csv_review.layout import types_tab, date_indexes_tab, select_main_date_column, date_indexes

##########################
#  Callbacks section     #
##########################

"""
@app.callback(
    Output('session-output-select-csv-output-table', 'children'),
    Input({'type': 'session-input-csv-review-date-show', 'index': ALL}, 'n_clicks'),
    State({'type': 'session-input-csv-review-date-column', 'index': ALL}, 'value'),
    State("data", "data")
)
def show_columns(buttons_clicks,columns_values, data):
    df = data
    #df = pd.read_json(data, orient='split')
    ctx = dash.callback_context
    if ctx.triggered:
        idx =  json.loads(ctx.triggered[0]["prop_id"].split(".")[0])["index"]
        col_name = columns_values[idx]

        try:
            dataframe = pd.concat([pd.to_datetime(df[col_name]), df[col_name]], axis=1)
            return dbc.Table.from_dataframe(dataframe, 
                                striped=True, 
                                borderless=True, 
                                hover=True, 
                                dark=False
            )
        except:
            print("error")

            try:
                return dbc.Table.from_dataframe(df[[col_name]], 
                                striped=True, 
                                borderless=True, 
                                hover=True, 
                                dark=False
                )
            except:
                return html.P("No data")

    return html.P("No data")
"""

"""
@app.callback(
    Output('select-csv-date-indexes-content', 'children'),
    Input('csv-review-date-column-radio','value'),
    State("data", "data")
)
def show_index_selection(value, data):
    df = data
    #df = pd.read_json(data, orient='split')
    columns_names = list(df.columns)
    aux =  [a for a in columns_names if len(a.split("_"))>1]
    temporal_indexers = list(set([a.split("_")[1] for a in aux]))
    temporal_variables =  set([a.split("_")[0] for a in aux])
    date_columns = [a for a in columns_names if re.findall("date", a, re.IGNORECASE)]

    if(value == "Main Date Column"):
        return select_main_date_column(date_columns)
    else:
        return date_indexes(df,columns_names, temporal_indexers, 
                    temporal_variables, date_columns)
"""

@app.callback(
    Output({'type': 'session-input-csv-review-date-div-popover-code','index': MATCH}, 'children'),
    Input({'type': 'session-input-csv-review-date-show-source', 'index': MATCH}, 'n_clicks'),
    State({'type': 'session-input-csv-review-date-format', 'index': MATCH}, 'id'),
)
def show_columns(n_clicks, idx):
    #df = pd.read_json(data, orient='split')
   
    
    b = dash_ace.DashAceEditor(
            id='input',
            value=
            '# available libraries: pandas (as pd), numpy (as np) \n'
            '# only function content will be parsed  \n '
            '# import inside function is not allowed  \n \n'
            'def test(a: int) -> str : \n'
            '   return f"value is {a}"',
            theme='monokai',
            mode='python',
            tabSize=2,
            enableBasicAutocompletion=True,
            enableLiveAutocompletion=True,
            autocompleter='/autocompleter?prefix=',
            placeholder='Python code ...',
            style={"height": "70rem", "width":"100%"}
        ) 
    
    return dbc.Popover(
        [
            dbc.PopoverHeader("Code Edition", style={"textAlign": "center"}),
            dbc.PopoverBody([
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            children=[
                                dbc.Label("Theme:")
                            ],
                            style = {'display': 'inline-block', "marginBottom": -12, "width":100, "paddingLeft": 20}
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    options=[{'label': 'monokai', 'value': 'monokai'}, 
                                            {'label': 'github', 'value': 'github'},
                                            {'label': 'tomorrow', 'value': 'tomorrow'},
                                            {'label': 'kuroir', 'value': 'kuroir'},
                                            {'label': 'twilight', 'value': 'twilight'},
                                            {'label': 'xcode', 'value': 'xcode'},
                                            {'label': 'textmate', 'value': 'textmate'},
                                            {'label': 'solarized_dark', 'value': 'solarized_dark'},
                                            {'label': 'solarized_light', 'value': 'solarized_light'},
                                            {'label': 'terminal', 'value': 'terminal'}
                                            ],
                                    value='monokai'            
                                )
                            ],
                            style = {'display': 'inline-block', "marginBottom": -12, "width":150}
                        ),
                    ],
                    style={"justifyContent": "center"}
                ),
                html.Br(),
                b, 
                html.Br(),
                html.Div(
                    html.Button(
                        children=["Test Code"], 
                        n_clicks=0, 
                        #style={"background": "red"}
                    ),
                    style={"textAlign": "center"}
                ),
                html.Br()
            ])
        ],
        target="show-source-csv-review-"+str(idx["index"]),
        is_open = bool(n_clicks %2),
        style = {"width": 1000, 'fontSize':12}
    )
    

@app.callback(
    Output({'type': 'session-input-csv-review-date-toast-button', 'index': MATCH}, 'children'),
    Input({'type': 'session-input-csv-review-date-toast-button', 'index': MATCH}, 'n_clicks'),
    State({'type': 'session-input-csv-review-date-toast-button', 'index': MATCH}, 'id'),
    State({'type': 'session-input-csv-review-date-toast-button', 'index': MATCH}, 'children')
)
def display_output(n_click,idx,children):
    if(n_click>0):
        return [html.I( 
                    id={"type": "session-input-csv-review-date-icon",
                        "index": idx["index"]
                    },
                    className="fas fa-check", 
                    style={"color": "green", "paddingLeft":10}
                )
        ]
    else:
        raise PreventUpdate

"""
@app.callback(
    Output('list-of-columns-csv-review-types', 'children'),
    State("data", "data")
)
def show_columns(buttons_clicks,columns_values, data):
    

    return html.P("No data")
"""