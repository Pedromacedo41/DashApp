# import main app object for callback registration
from app import app 

# import of internal modules
from pages.csv_dashboard.layout import tab1, tab2
import datetime

# import of external libraries
import dash
from dash.dependencies import Input, Output, State, ALL, MATCH
from dash.exceptions import PreventUpdate
import dash_html_components as html
import dash_bootstrap_components as dbc
from pages.csv_dashboard.layout import build_tabs
from dash_extensions.enrich import Trigger
from dash_extensions.enrich import ServersideOutput
from sqlite3 import connect

import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

import json
import pandas as pd
import plotly.graph_objs as go
import re
import os
import time
import sys
import traceback
import base64
import io


##########################
#  Callbacks section     #
##########################


@app.callback(
    Output("download-session", "data"),
    Trigger("save-session-button", "n_clicks"),
    State("custom_data_session", "data"),
    prevent_initial_call=True
)
def func(my_dict):
    return dict(content= json.dumps(my_dict), filename="session.json")


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


"""
@app.callback(Output("variable-list-container", "children"),
              Trigger("variable-list-add", "n_clicks"),
              State("variable-list-container", "children"),
              State("data_df", "data"),
              prevent_initial_update=True)
def generate_plot(children, data):
    columns = data.columns
    idx= 0 if children is None else len(children)
    new_list = html.Div(
            className="twelve columns",
            children=[
                html.Div(
                    children= [
                        dcc.Input(
                            type="text",
                            id={"type": "variable-list-type-text",
                                "index": idx
                            },
                            placeholder="list name..",
                            value = "list_" + str(idx),
                            style={"background": "#1E2130", "color": "white"}
                        )
                    ],
                    style = {'display': 'inline-block', "marginBottom": -12, "width":40}  
                ),
                html.Div(
                    dcc.Dropdown(
                        id={"type": 'variable-list-type-dropdown',
                            "index": idx
                        },
                        options=[{"label": a, "value": a} for a in columns],
                        value=[columns[0]],
                        multi= True
                    ),
                    style = {'display': 'inline-block', "marginBottom": -12, "width":600, "marginLeft": 180}  
                ),
                html.Div(
                    html.Button(
                        id={"type": "variable-list-type-view-buttom",
                            "index": idx
                        },
                        children="View",
                        n_clicks=0
                    ), 
                    style={'display': 'inline-block', "marginBottom": -12, "paddingLeft": 30 }
                ),
                html.Div(
                    dbc.Button(
                        id={"type": "variable-list-type-delete-buttom",
                            "index": idx
                        },
                        children=[html.I(className="fas fa-trash mr-2", style={"color": "red", })],
                        n_clicks=0,
                        style={"fontSize":"1.8rem","background": "none","border": "none", "marginBottom": 10}
                    ), 
                    style={'display': 'inline-block'}
                ),
                html.Div(
                    children=[
                        html.Div(
                            dbc.Button(
                                id={"type": "variable-list-type-up-buttom",
                                    "index": idx
                                },
                                children=[html.I(className="fas fa-chevron-up mr-2", style={"color": "white"})],
                                n_clicks=0,
                                style={"fontSize":"1rem","background": "none","border": "none", "marginBottom": -25}
                            ),
                        ),
                        html.Div(
                            dbc.Button(
                                id={"type": "variable-list-type-down-buttom",
                                    "index": idx
                                },
                                children=[html.I(className="fas fa-chevron-down mr-2", style={"color": "white"})],
                                n_clicks=0,
                                style={"fontSize":"1rem","background": "none","border": "none", "marginBottom": -11}
                            )
                        )
                    ],
                    style={'display': 'inline-block'}
                )
            ]
    )
    a= children
    if(a is None):
        return [new_list]
    else:
        a.append(new_list)
        return a
"""

@app.callback(
    Output("table-csv-dashboard-data-vis", "options"),
    Input("custom_data_session", "data"),
    prevent_initial_update=True
)
def show_list(my_dict):
    if(my_dict is not None):
        my_list = []
        if "sql-request" in my_dict:
            for idx, value in enumerate(my_dict["sql-request"]):
                if(value["status"]):
                    my_list.append({'label': value["timestamp"], 'value': value["timestamp"]})

        return my_list
    return []



@app.callback(
    ServersideOutput("custom_data_session", "data"),
    #Output("sql-dataframe-result", "data"),
    #Output("sql-dataframe-result", "columns"),
    Output("log_textarea", "value"),
    Input('request-run', 'n_clicks'),
    State('ace_editor_sql', 'value'),
    State("custom_data_session", "data"),
    State("data", "data"),
    prevent_initial_update=True
)
def show_columns(n_clicks,value, session_dict, data):
    if(n_clicks>0):
        if(session_dict is not None):
            dic = session_dict.copy()
        else:
            dic = {}

        conn = connect(':memory:')
        data.to_sql('df', con=conn)
        success = True
        log = "Success"

        try:
            datak = pd.read_sql(value, conn)
            
        except:
            success = False
            log = "".join(traceback.format_exception(*sys.exc_info(), chain=True))

        if "sql-request" in dic:
            dic["sql-request"].append({"status": success, "request": value, "log": log, "timestamp": time.time()})
        else:
            dic["sql-request"] = [{"status": success, "request": value, "log": log,  "timestamp": time.time()}]
        
        if(success):
            print("here")
            dic["sql-request"][-1]["data"] = datak
            print("herekkk")
            #return dic, datak.to_dict("records"), [{"name": i, "id": i} for i in datak.columns], log
            return dic, log
        else:
            #return dic, pd.DataFrame().to_dict("records"), [], log
            return dic, log
    else:
        raise PreventUpdate


@app.callback(
    ServersideOutput("custom_data_session", "data"),
    Input('clear-all-requests', 'n_clicks'),
    State("custom_data_session", "data"),
    prevent_initial_update=True
)
def show_columns(n_clicks, session_dict):
    if(n_clicks>0):
        if(session_dict is not None):
            dic = session_dict.copy()
        else:
            dic = {}   
        
        dic["sql-request"] = []
        return dic
    else:
        raise PreventUpdate


@app.callback(
    ServersideOutput("custom_data_session", "data"),
    Input('clear-all-failed-requests', 'n_clicks'),
    State("custom_data_session", "data"),
    prevent_initial_update=True
)
def show_columns(n_clicks, session_dict):
    if(n_clicks>0):
        if(session_dict is not None):
            dic = session_dict.copy()
        else:
            dic = {}   
        
        new_list = []
        for idx, value in enumerate(dic["sql-request"]):
            if(value["status"]) :
                new_list.append(value)

        dic["sql-request"]= new_list
        return dic
    else:
        raise PreventUpdate


@app.callback(
    Output("requests-list-container", "children"),
    Input("custom_data_session", "data"),
)
def show_columns(session_dict):
    if "sql-request" in session_dict:
        children = []
        for idx,value in enumerate(session_dict["sql-request"]):
            icon = "fas fa-check mr-2" if value["status"] else "fas fa-times mr-2"
            color = "green" if value["status"] else "red"
            a = html.Div(
                    className="twelve columns",
                    children=[
                        html.Div(
                            className="one columns",
                            children= [
                                html.I(className=icon, style={"color": color})
                            ]
                        ),
                        html.Div(
                            className="two columns",
                            children= [
                                str(pd.Timestamp(value["timestamp"],unit="s"))
                            ],
                            style={"fontSize": 11}
                        ),
                        html.Div(
                            className="two columns",
                            children= [
                                dcc.Input(
                                    type="text",
                                    id={"type": "request-list-name",
                                        "index": idx
                                    },
                                    placeholder="request name..",
                                    value = "req_"+str(idx),
                                    disabled=True,
                                    style={"background": "black", "color": "white", "border": "none", "width": "100%", "fontSize": 12}
                                )
                            ],
                        ),
                        html.Div(
                            className="four columns",
                            children=[
                                dcc.Textarea(
                                    id={"type": 'request-list-value',
                                        "index": idx
                                    },
                                    value=value["request"],
                                    disabled=True,
                                    style={"background": "white", "color": "black", "width": "100%", "border": "none", "fontSize": 12, "height":30}, 
                                )
                            ]
                            #style = {'display': 'inline-block', "marginBottom": -12, "width":300, "marginLeft": 180}  
                        ),
                        html.Div(
                            className="three columns",
                            children=[
                                html.Div(
                                    dbc.Button(
                                        id={"type": "request-list-type-vieww-buttom",
                                            "index": idx
                                        },
                                        children=[html.I(className="fas fa-eye mr-2", style={})],
                                        n_clicks=0,
                                        style={"fontSize":"1.6rem","background": "none","border": "none", "marginBottom": 8, "marginRight":0}
                                    ), 
                                    style={'display': 'inline-block'}
                                ),
                                html.Div(
                                    dbc.Button(
                                        id={"type": "request-list-type-delete-buttom",
                                            "index": idx
                                        },
                                        children=[html.I(className="fas fa-trash mr-2", style={})],
                                        n_clicks=0,
                                        style={"fontSize":"1.6rem","background": "none","border": "none", "marginBottom": 8, "marginRight":0}
                                    ), 
                                    style={'display': 'inline-block'}
                                ),
                                html.Div(
                                    dbc.Button(
                                        id={"type": "request-list-type-edit-buttom",
                                            "index": idx
                                        },
                                        children=[html.I(className="fas fa-edit mr-2", style={})],
                                        n_clicks=0,
                                        style={"fontSize":"1.6rem","background": "none","border": "none", "marginBottom": 8, "marginRight":0}
                                    ), 
                                    style={'display': 'inline-block'} if value["status"] else {'display': 'inline-block', "display": "none"}
                                ),
                                html.Div(
                                    dbc.Button(
                                        id={"type": "request-list-type-download-buttom",
                                            "index": idx
                                        },
                                        children=[html.I(className="fas fa-download mr-2", style={})],
                                        n_clicks=0,
                                        style={"fontSize":"1.6rem","background": "none","border": "none", "marginBottom": 8, "marginRight":0}
                                    ), 
                                    style={'display': 'inline-block'} if value["status"] else {'display': 'inline-block', "display": "none"}
                                ),
                            ],
                            style={"justifyContent": "right"}
                        )
                    ]
                )
        
            children.append(a)

        return children

    else:
        return [
            html.Br(),
            html.P("No saved request")
        ]
            
"""
@app.callback(
    Output("variable-list-container", "children"),
    Input("url", "pathname"),
    State("var-list", "data"),
    State("data", "data"))
def init_list(pathname, dic, data):
    if pathname == "/variable-list-creation":
        print("i am heree")
        print(dic)
        print("i am out of here")
        children = []
        columns = data.columns
        for idx,value in enumerate(dic):
            a = html.Div(
                    className="twelve columns",
                    children=[
                        html.Div(
                            children= [
                                dcc.Input(
                                    type="text",
                                    id={"type": "variable-list-type-text",
                                        "index": idx
                                    },
                                    placeholder="list name..",
                                    value = value,
                                    style={"background": "#1E2130", "color": "white"}
                                )
                            ],
                            style = {'display': 'inline-block', "marginBottom": -12, "width":40}  
                        ),
                        html.Div(
                            dcc.Dropdown(
                                id={"type": 'variable-list-type-dropdown',
                                    "index": idx
                                },
                                options=[{"label": a, "value": a} for a in columns],
                                value=dic[value],
                                multi= True
                            ),
                            style = {'display': 'inline-block', "marginBottom": -12, "width":600, "marginLeft": 180}  
                        ),
                        html.Div(
                            html.Button(
                                id={"type": "variable-list-type-view-buttom",
                                    "index": idx
                                },
                                children="View",
                                n_clicks=0
                            ), 
                            style={'display': 'inline-block', "marginBottom": -12, "paddingLeft": 30 }
                        ),
                        html.Div(
                            dbc.Button(
                                id={"type": "variable-list-type-delete-buttom",
                                    "index": idx
                                },
                                children=[html.I(className="fas fa-trash mr-2", style={"color": "red", })],
                                n_clicks=0,
                                style={"fontSize":"1.8rem","background": "none","border": "none", "marginBottom": 10}
                            ), 
                            style={'display': 'inline-block'}
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    dbc.Button(
                                        id={"type": "variable-list-type-up-buttom",
                                            "index": idx
                                        },
                                        children=[html.I(className="fas fa-chevron-up mr-2", style={"color": "white"})],
                                        n_clicks=0,
                                        style={"fontSize":"1rem","background": "none","border": "none", "marginBottom": -25}
                                    ),
                                ),
                                html.Div(
                                    dbc.Button(
                                        id={"type": "variable-list-type-down-buttom",
                                            "index": idx
                                        },
                                        children=[html.I(className="fas fa-chevron-down mr-2", style={"color": "white"})],
                                        n_clicks=0,
                                        style={"fontSize":"1rem","background": "none","border": "none", "marginBottom": -11}
                                    )
                                )
                            ],
                            style={'display': 'inline-block'}
                        )
                    ]
                )
        
            children.append(a)

        return children

    else:
        raise PreventUpdate
"""

@app.callback(
    ServersideOutput("var-list", "data"),
    Input({'type': 'variable-list-type-text', 'index': ALL}, 'value'),
    Input({'type': 'variable-list-type-dropdown',    'index': ALL}, 'value')
)
def show_columns(names,values):
    my_dict = {}
    for a in range(len(names)):
        my_dict[names[a]]= values[a]

    print(len(my_dict))
    if len(my_dict) <2:
        raise PreventUpdate
    else:
        print(my_dict)
        return my_dict



@app.callback(
    Output("ace_editor_sql", "theme"),
    Input("dropdwon-theme-ace-editor-sql", 'value'),
)
def show_columns(value):
    return value




@app.callback(
    Output("ace_editor_sql", "value"),
    Output("log_textarea", "value"),
    Input({'type': "request-list-type-vieww-buttom", 'index': ALL}, 'n_clicks'),
    State("custom_data_session", "data"),
    prevent_initial_call=True
)
def show_columns(values, session_dict):
    ctx = dash.callback_context

    if ctx.triggered:
        idx = int(json.loads(ctx.triggered[0]['prop_id'].split('.')[0])["index"])
        if(ctx.triggered[0]['value'] > 0):
            return session_dict["sql-request"][idx]["request"], session_dict["sql-request"][idx]["log"]
        else:
            raise PreventUpdate

    return dash.no_update, dash.no_update

## finish #
@app.callback(
    ServersideOutput("custom_data_session", "data"),
    Input({'type': "request-list-type-delete-buttom", 'index': ALL}, 'n_clicks'),
    State("custom_data_session", "data"),
    prevent_initial_call=True
)
def show_columns(values, session_dict):
    ctx = dash.callback_context

    if ctx.triggered:
        idx = int(json.loads(ctx.triggered[0]['prop_id'].split('.')[0])["index"])
        if(ctx.triggered[0]['value'] > 0):
            dic = session_dict.copy()
            list_copy = session_dict["sql-request"].copy()
            list_copy.pop(idx)
            dic["sql-request"] = list_copy
            return dic
        else:
            raise PreventUpdate

    return dash.no_update, dash.no_update
    

"""
@app.callback(Output("box-plot", "figure"),
              Input("input-session-demo-dropdown", "value"),
              State("data", "data"))
def generate_plot(value, data):
    df = data
    #df = pd.read_json(data, orient='split')
    columns_names = list(df.columns)
    aux =  [a for a in columns_names if len(a.split("_"))>1]
    temporal_indexers = list(set([a.split("_")[1] for a in aux]))

    fig = go.Figure()

    if(value is not None):
        for elem in temporal_indexers:
            name = value + "_"+ elem
            fig.add_trace(go.Box(y=df[name], name = name))

        fig.update_layout(title = value)
    fig.update_layout(yaxis_title='Value', template= "plotly_dark")
    
    return fig
"""
