# import of external libraries
import dash_daq as daq
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import re

# import of internal libraries
from utils import make_big_tab,  make_row, make_column, make_mini_tab


def generate_list_of_columns(columns_names, init):
    children = []
    for i, a in enumerate(columns_names[init: (init+15) if (init+15)<len(columns_names) else len(columns_names)]):
        children.append(
            html.Div(
                className="row",
                children=[
                    html.Div(
                        className="six columns",
                        children=[
                            html.Div(
                                dbc.Label(a),
                                style = {'display': 'inline-block', "marginBottom": -12, "width":250, "paddingLeft":30}
                            ),
                            html.Div(
                                dcc.Dropdown(
                                    id={"type": "session-input-csv-review-type-dropdown",
                                        "index": i+init
                                        },
                                    options=[{'label': 'numeric', 'value': 'numeric'}, 
                                            {'label': 'string', 'value': 'string'},
                                            {'label': 'date', 'value': 'date'}
                                            ],
                                    value='numeric'
                                    
                                ),
                                style = {'display': 'inline-block', "marginBottom": -12, "width":150}
                            ),
                            html.Div(
                                html.Button(
                                    id={"type": "session-input-csv-review-type-show",
                                        "index": i+init
                                    },
                                    children="Show", 
                                    n_clicks=0
                                ), 
                                style={'display': 'inline-block', 'margin': "0 10px"}
                            ),
                            html.Div(
                                id="info-div-csv-review-date"+str(i+init),
                                children=[
                                    html.I( 
                                        id={"type": "session-input-csv-review-type-icon",
                                            "index": i+init
                                            }
                                    ),
                                    html.Div(
                                        id={"type": "session-input-csv-review-type-div-popover",
                                            "index": i+init
                                        }
                                    )
                                ],
                                style={'display': 'inline-block', 'margin': "0 10px"}
                            )
                        ]
                    ),
                    html.Div(
                        className="four columns",
                        children=[
                            html.Div(
                                dcc.Dropdown(
                                    id={"type": "session-input-csv-review-date-format",
                                        "index": i
                                        },
                                    options=[{'label': 'inferred', 'value': 'infer'}, 
                                            {'label': 'ddmmyyyy', 'value': 'ddmmyyyy'},
                                            {'label': 'dd-mm-yyyy', 'value': 'ddmmyyyy'},
                                            {'label': 'mmddyyyy', 'value': 'ddmmyyyy'},
                                            {'label': 'mm-dd-yyyy', 'value': 'ddmmyyyy'},
                                            ],
                                    value='infer'
                                    
                                ),
                                style = {'display': 'inline-block', "marginBottom": -12, "width":150}
                            )
                        ]
                    ),
                    html.Div(
                        className="two columns",
                        children=[
                            html.Div(
                                id = "show-source-csv-review-"+str(i),
                                children = [
                                    html.Button(
                                        id={"type": "session-input-csv-review-date-show-source",
                                            "index": i  
                                        },
                                        children="source", n_clicks=0
                                    ),
                                    html.Div(
                                        id={"type": "session-input-csv-review-date-div-popover-code",
                                            "index": i
                                        }
                                    )
                                ], 
                                style={'display': 'inline-block', 'margin': "0 10px"}
                            )
                        ]
                    )
                ]
            )
        )

    return children


def types_tab(df,columns_names, temporal_indexers, temporal_variables, date_columns):
    numeric, date, ch_variable = [], [], []
    children = [
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="12 columns",
                    children =dbc.Label( "Showing columns 1-15 of "+ str(len(columns_names)) ,id="csv-review-label")
                )
            ],
            style={"textAlign": "center"}
        ),
        html.Div(
            className="row",
            children=[
                html.Div(
                    className="12 columns",
                    children =[
                        html.Div(
                            children = [
                                dbc.Button(
                                    id = "back-button-csv-review-type",
                                    children =html.I(className="fas fa-arrow-left"),
                                    outline = False,
                                    style = {'display': 'inline-block', "marginBottom": -12, "width": 25, "textAlign": "center"}
                                ),
                                dbc.Button(
                                    id = "forward-button-csv-review-type",
                                    children =html.I(className="fas fa-arrow-right"),
                                    outline = False,
                                    style = {'display': 'inline-block', "marginBottom": -12, "width": 25, "textAlign": "center"}
                                ),
                            ]
                        )
                    ]
                )
            ],
            style={"textAlign": "center"}
        ),
        html.Br(),
        html.Br(),
        html.Div(
            className="row",
            style={"paddingLeft": 30},
            children=[
                html.Div(className="six columns",children = [html.Label("Column Types"), html.Br()]),
                html.Div(className="four columns",children = [html.Label("Data Tools"), html.Br()]),
                html.Div(className="two columns",children = [html.Label("Source Tools"), html.Br()])
            ]
        ),
        html.Div(
            id="list-of-columns-csv-review-types",
            children = generate_list_of_columns(columns_names, 0)
        )
    ] 


    return [html.Div(
        children = children
    )]

    


def date_indexes(df,columns_names, temporal_indexers, 
                    temporal_variables, date_columns):
    list_indexer_childrens = [html.Br()]

    a = html.Div(
        className="row",
        style={"paddingLeft": 50},
        children=[
            html.Div(className="four columns",children = [html.Label("Date Index"), html.Br()])
        ])
           # [html.Label("Date_indexer", style = {'display': 'inline-block', "width":150}),
           # html.Label("Date column", style = {'display': 'inline-block', "marginBottom": -12, "width":400 }),
           # html.Label("Date format", style = {'display': 'inline-block', "marginBottom": -12, "width":240})
           # ])
    list_indexer_childrens.append(a)
    for i in range(len(temporal_indexers)):
        a= html.Div(
            className="row",
            style={"paddingLeft": 50},
            children=[
                html.Div(
                    className="twelve columns",
                    children=[
                        dbc.Checklist(
                            options=   [ {'label': "   "+ temporal_indexers[i], 'value': temporal_indexers[i]} ],
                            value= [temporal_indexers[i]],
                            id={"type": "session-input-csv-review-date-checklist",
                                        "index": i
                            },
                            style = {"fontWeight": 1.2, 'display': 'inline-block', "width":80}
                        ),
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id={"type": "session-input-csv-review-date-column",
                                        "index": i
                                    },
                                    options=[{'label': a, 'value': a} for a in date_columns],
                                    value='Date_'+ temporal_indexers[i],
                                    
                                )
                            ],
                            style = {'display': 'inline-block', "marginBottom": -12, "width":200}
                        ),
                        html.Div(
                            html.Button(
                                id={"type": "session-input-csv-review-date-show",
                                    "index": i
                                },
                                children="Show", n_clicks=0
                            ), 
                            style={'display': 'inline-block', 'margin': "0 10px"}
                        )
                    ]
                )
            ]
        )

        

        list_indexer_childrens.append(a)
        

    return list_indexer_childrens


def date_indexes_tab(df,columns_names, temporal_indexers, 
                    temporal_variables, date_columns):
    children = [
        html.Br(),
        html.Br(),
        html.Div(
            dcc.RadioItems(
                id= "csv-review-date-column-radio",
                options=[
                    {'label': '   Main Date Column', 'value': 'Main Date Column'},
                    {'label': '   Date Indexes', 'value': 'Date Indexes'}
                ],
                value='Main Date Column',
                labelStyle= {"paddingLeft": 30}
            )
        ),
        html.Br(),
        html.Div(id="select-csv-date-indexes-content", style={"padding": 20})
    ]
    return children


def select_main_date_column(date_columns):
    return [
         html.Div(
            dcc.Dropdown(
                id="session-input-csv-review-date-format",
                options=[{"label": a, "value": a} for a in date_columns],
                value=date_columns[0]
            ),
            style = {'display': 'inline-block', "marginBottom": -12, "width":150}  
        )
    ]


def csv_review(data):
    """
    uppermost layout of csv_review page
    """
    df = data
    #df = pd.read_json(data, orient='split')
    columns_names = list(df.columns)
    aux =  [a for a in columns_names if len(a.split("_"))>1]
    temporal_indexers = list(set([a.split("_")[1] for a in aux]))
    temporal_variables =  set([a.split("_")[0] for a in aux])
    date_columns = [a for a in columns_names if re.findall("date", a, re.IGNORECASE)]

    tabs = [dbc.Tabs([
                make_mini_tab(date_indexes_tab(df,columns_names, temporal_indexers, 
                    temporal_variables, date_columns), "Date Columns and Indexes"),
                make_mini_tab(types_tab(df,columns_names, temporal_indexers, temporal_variables, date_columns), "Types")
            ]
        )
    ]

    children2 = [
        html.Div(
            id="session-output-select-csv-output-table",
            style={"overflow-y": "scroll", "overflow-x": "scroll","height": "75rem"}
        )
    ]

    return [html.Div(html.H3("Table Review"), style={"align": "center"}),
            html.Br(),
            make_row([
                make_column(8, tabs, "Topics"),
                make_column(4, children2, "Column View", border_left=True)
            ]),
            html.Br(),
            html.Div([
                html.Button(id="change-page-button-csv-review", children="SUBMIT", n_clicks=0),
            ], style={"textAlign": "center"})
    ]