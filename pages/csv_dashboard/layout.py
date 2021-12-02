# import of external libraries
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_ace
import dash_table


import pandas as pd
import re

# import of internal modules
from utils import make_big_tab,  make_row, make_column, make_mini_tab, return_box
from datetime import date
from gridlayout import GridLayout


def sql_tool(data):
    


    b = dash_ace.DashAceEditor(
            id='ace_editor_sql',
            value=
            'SELECT * FROM df as T',
            theme='monokai',
            syntaxKeywords = {
                "variable.language":  "select|insert|update|delete|from|where|and|or|group|by|order|limit|offset|having|as|case|" +
                                      "when|then|else|end|type|left|right|join|on|outer|desc|asc|union|create|table|primary|key|if|" +
                                      "foreign|not|references|default|null|inner|cross|natural|database|drop|grant|SELECT|INSERT|UPDATE|DELETE|FROM|WHERE|AND|OR|GROUP|BY|ORDER|LIMIT|OFFSET|HAVING|AS|CASE|" +
                                      "WHEN|THEN|ELSE|END|TYPE|LEFT|RIGHT|JOIN|ON|OUTER|DESC|ASC|UNION|CREATE|TABLE|PRIMARY|KEY|IF|" +
                                      "FOREIGN|NOT|REFERENCES|DEFAULT|NULL|INNER|CROSS|NATURAL|DATABASE|DROP|GRANT",
                "support.function": "avg|count|first|last|max|min|sum|ucase|lcase|mid|len|round|rank|now|format|coalesce|ifnull|isnull|nvl|AVG|COUNT|FIRST|LAST|MAX|MIN|SUM|UCASE|LCASE|MID|LEN|ROUND|RANK|NOW|FORMAT|COALESCE|IFNULL|ISNULL|NVL",
                "support.type": "int|numeric|decimal|date|varchar|char|bigint|float|double|bit|binary|text|set|timestamp|money|real|number|integer|INT|NUMERIC|DECIMAL|DATE|VARCHAR|CHAR|BIGINT|FLOAT|DOUBLE|BIT|BINARY|TEXT|SET|TIMESTAMP|MONEY|REAL|NUMBER|INTEGER",
                "storage.modifier": "parameter|atomic|primary|optional|id|time|asc|desc|PARAMETER|ATOMIC|PRIMARY|OPTIONAL|ID|TIME|ASC|DESC|",
                "constant.language": "true|false|TRUE|FALSE"
            },
            mode='mysql',
            tabSize=2,
            fontSize=15,
            enableBasicAutocompletion=True,
            enableLiveAutocompletion=True,
            autocompleter='/autocompleter?prefix=',
            placeholder='sql code ...', 
            style={"height":40, "width":"100%"}
    ) 

    children1= [
        html.Br(),
        html.Div(
            className="row",
            children=[
                html.Div(
                    children=[
                        dbc.Label("Theme:", style={"fontSize":12})
                    ],
                    style = {'display': 'inline-block', "marginBottom": -12, "width":80, "paddingLeft": 20}
                ),
                html.Div(
                    children=[
                        dcc.Dropdown(
                            id= "dropdwon-theme-ace-editor-sql",
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
                            value='github',
                            style={"fontSize":12}           
                        )
                    ],
                    style = {'display': 'inline-block', "marginBottom": -12, "width":150}
                ),
            ],
            style={"justifyContent": "left"}
        ),
        html.Br(),
        b, 
        html.Br(),
        html.Div(
            html.Button(
                id = "request-run",
                className="btn-dark",
                children=["Run Request"], 
                n_clicks=0, 
                #style={"background": "red"}
            ),
            style={"textAlign": "center"}
        ),
        html.Br()
    ]

    children5 = [
        html.Br(),
        html.Div(
            className="twelve columns",
            children=[
                dcc.Textarea(
                    id="log_textarea",
                    placeholder="Log message",
                    disabled=False,
                    value="eetete",
                    style={"background": "white", "color": "black", "width": "100%", "border": "none", "fontSize": 12, "height": "100%"}, 
                )
            ]
        )
    ]

    children4 = dbc.Tabs([
         make_mini_tab(children5, "Log"),
         make_mini_tab("test", "Output")
    ])

    children2 = [
        make_row([
            make_column(12,[
                html.Div(
                    dbc.Button(
                        id="clear-all-requests",
                        className= "btn-dark",
                        children="Clear all",
                        n_clicks=0
                    ), 
                    style={'display': 'inline-block'}       
                ),
                html.Div(
                    dbc.Button(
                        id="clear-all-failed-requests",
                        className= "btn-dark",
                        children="Clear failed",
                        n_clicks=0
                    ), 
                    style={'display': 'inline-block'}       
                ),
                html.Div(
                    children=[
                        html.Div([
                            dcc.DatePickerRange(
                                id='my-date-picker-range',
                                min_date_allowed=date(1995, 8, 5),
                                max_date_allowed=date(2017, 9, 19),
                                initial_visible_month=date(2017, 8, 5),
                                end_date=date(2017, 8, 25),
                                day_size=50,
                            ),
                            html.Div(id='output-container-date-picker-range', style={"fontSize": 12})
                        ])
                    ],
                    style={'display': 'inline-block'}       
                ),
                html.Br(),
                html.Br(),
                html.Div(
                    html.Div(
                        className="twelve columns",
                        children=[
                            html.Div(
                                className="one columns",
                                children=[dbc.Label("Status", style={"fontSize": 13})]
                            ),
                            html.Div(
                                className="two columns",
                                children=[dbc.Label("Date", style={"fontSize": 13})]
                            ),
                            html.Div(
                                className="two columns",
                                children=[dbc.Label("Name", style={"fontSize": 13})]
                            ),
                            html.Div(
                                className="four columns",
                                children=[dbc.Label("Query/Code", style={"fontSize": 13})]
                            ),
                            html.Div(
                                className="three columns",
                                children=[dbc.Label("Options", style={"fontSize": 13})]
                            )
                        ]
                    )
                ),
                html.Hr(style={"borderTop": "0.1px solid #FFFFFF1F", "marginBottom": "1.5rem"}),
                html.Div(
                    id="requests-list-container",
                    style={"overflow-y": "scroll", "height": "30rem"}
                )
            ])
        ])
    ]
    
    
    children3 = html.Div(
            children=dash_table.DataTable(id="sql-dataframe-result"), 
            style={"background": "white", "color": "red", "overflow-y": "scroll", "overflow-x": "scroll","height": "75rem"}
    )
    

    return [html.Div(html.H5("SQL Tool"), style={"align": "center"}),
            html.Div(
                children=[
                    GridLayout(
                        id='inputt',
                        layout= [{"i": 'a', "x": 0, "y": 0,"h":4, "w": 6, "minW": 2},
                                {"i": 'b', "x": 1, "y": 0, "w": 6, "h":4, "minW": 2},
                                {"i": 'c', "x": 2, "y": 2, "w": 2, "h":4, "minW": 2},
                                {"i": 'd', "x": 4, "y": 3, "w": 12, "h":4, "minW": 2}],
                        children=[
                            return_box("Code Editor", children1,1),
                            return_box("Past Requests", children2,5),
                            return_box("Outputs", children4,6),
                            return_box("Table", children3,7)
                        ]
                    )
                ],
                style={"padding": 0}
            )
    ]


def data_vis(data):

    children = [html.Div(
            className="row",
            style={"paddingLeft": 50, "paddingTop": 50},
            children=[
                html.Div(
                    className="twelve columns",
                    children=[
                        html.Div(
                            children=[
                                dcc.Dropdown(
                                    id={"type": "sesssscolumn",
                                        "index": 1
                                    },
                                    options=[{'label': str(a) + " variables" , 'value': a} for a in range(1,5)],
                                    value="1 variables",
                                )
                            ],
                            style = {'display': 'inline-block', "marginBottom": -12, "width":200}
                        ),
                        html.Div(
                            dbc.Button(
                                id={"type": "dtass",
                                    "index": 1
                                },
                                children=[
                                    "Go"
                                ],
                                n_clicks=0,
                                className="success"
                            ), 
                            style={'display': 'inline-block', 'margin': "0 10px"}
                        )
                    ]
                )
            ]
        )]

    return html.Div(
        #id="tabs",
        style = {"width": "100%"},
        #className="tabs",
        children = [
            html.Div(
                children=[
                    html.Div(
                        children= [dbc.Label("Table:", 
                                            style=  {"width": 80}
                                        )
                                  ],
                        style={"display": "inline-block", "marginBottom": -12}
                    ),
                    html.Div(
                        children=[
                            dcc.Dropdown(
                                id="table-csv-dashboard-data-vis",
                                style={"width": 240, "fontSize":12}
                            )
                        ],
                        style={"display": "inline-block", "marginBottom": -12}
                    ),
                ], 
                style={"width": "100%", "textAlign": "center"}
            ),
            #dbc.Tabs([
            #    make_mini_tab(pivot_table(data), "One Variable"),
            #    make_mini_tab(pivot_table(data), "Two Variables")
            #]),
            html.Div(
                children=[
                    GridLayout(
                        id='inputt',
                        layout= [{"i": 'a', "x": 0, "y": 0,"h":8, "w": 6, "minW": 2},
                                {"i": 'b', "x": 7, "y": 0, "w": 6, "h":8, "minW": 2}],
                        children=[
                            return_box("Data Visualization", [html.P("tee")],9, has_delete=True),
                            return_box("Data Visualization", children,10, has_delete=True)
                        ]
                    )
                ],
                style={"padding": 0}
            )
        ]
    )

def pivot_table(data):
    children1= html.Div(
                    children=[
                        html.Div(
                            children=[
                                dbc.Label("Variable:",
                                    style = {"width": 80}
                                )
                            ],
                            style={"display": "inline-block", "paddingLeft": 30,  "marginBottom": -12}
                        ),
                        html.Div(
                            children =[
                                dcc.Dropdown(
                                    id="histogram-csv-dashboard",
                                    style={"width": 240, "fontSize":12}
                                )
                            ],
                            style={"display": "inline-block",  "marginBottom": -12}
                        )
                    ],
                    style={"width": "100%"}
                )

    return [
        html.Div(
            style = {"width": "100%", "paddingLeft": 20},
            children = [
                html.Br(),
                make_row([
                    make_column(3, children1, "Options"),
                    make_column(9, "test", "Plot", border_left = True)
                ])
            ]
        )
    ]

def variables_list():
    return [
        html.Div(
            id="variable-list-container"
        ),
        html.Br(),
        html.Div(
            children=[
                html.Button(
                    id="variable-list-add",
                    children="Add list",
                    n_clicks=0,
                    style={"background":"green"}
                )
            ],
            style={"textAlign": "center", "marginTop": 30}
        )
    ]
    
                  
def build_variab_list():
    children2 = [
        html.Div(
            id="variable-list-output-table",
            style={"overflow-y": "scroll", "overflow-x": "scroll","height": "75rem"},
            children=[
                html.Div(id='output')
            ]
        )
    ]

    return [html.Div(html.H5("Variable Lists"), style={"align": "center"}),
            make_row([
                make_column(8, variables_list(), "Lists"),
                make_column(4, children2, "Table View", border_left=True)
            ])
    ]


def build_tabs(data):
    return html.Div(
        #id="tabs",
        style = {"width": "100%"},
        #className="tabs",
        children = [
            dbc.Tabs([
                make_mini_tab(my_tab1(data), "Test 1"),
                make_mini_tab("test 2", "Types")
            ])
        ]
    )


def my_tab1(data):
    return [
        html.Div(
            style = {"width": "100%", "paddingLeft": 20},
            children = [
                html.Br(),
                html.P("Test")
            ]
        )
    ]

def tab1(data_session, data):
    df = pd.read_json(data, orient='split')
    columns_names = list(df.columns)
    aux =  [a for a in columns_names if len(a.split("_"))>1]
    temporal_indexers = list(set([a.split("_")[1] for a in aux]))
    temporal_variables =  set([a.split("_")[0] for a in aux])
    date_columns = [a for a in columns_names if re.findall("date", a, re.IGNORECASE)]


    tab1_content = dcc.Graph(id="box-plot")
    tab2_content = [dcc.Dropdown(
            id="input-session-demo-dropdown-test1",
            options=[{"label": a, "value": a} for a in temporal_variables],
            value= data_session["demo-dropdown-value"] if data_session["status"]==1 else None,
            style={"width": 240}
        )]
    tab3_content = [dcc.Dropdown(
            id="input-session-demo-dropdown-test2",
            options=[{"label": a, "value": a} for a in temporal_variables],
            value= data_session["demo-dropdown-value"] if data_session["status"]==1 else None,
            style={"width": 240}
        )]

    tabs = dbc.Tabs(
        [
            make_mini_tab(tab1_content, label="Box Plot"),
            make_mini_tab(tab2_content, label="Box Plot2"),
            make_mini_tab(tab3_content, label="Box Plot3"),
        ]
    )
    
    children1 = [
        dcc.Dropdown(
            id="demo-dropdown",
            options=[{"label": a, "value": a} for a in temporal_variables],
            value= data_session["demo-dropdown-value"] if data_session["status"]==1 else None,
            style={"width": 240}
        )
    ]

    children2 = [
        tabs
    ]       
    return [    
            html.Div(
                children=[
                    GridLayout(
                        id='inputt',
                        layout= [{"i": 'a', "x": 0, "y": 0,"h":1, "w": 4, "minW": 2},
                                {"i": 'b', "x": 1, "y": 0, "w": 8, "h":1, "minW": 2}],
                        children=[
                            return_box("Control Panel", children2,1)
                        ]
                    )
                ],
                style={"backgroundColor": "#C5D2DE"}
            )
                #make_row([
                #    make_column(4, children1, "Control Panel"), 
                #    make_column(8, children2, "Graphics", border_left=True)
                #])
    ]


def tab2():
    children=[
            dcc.Dropdown(
                id="demo-dropdown2",
                options=[{"label": "aa", "value": "aaa"}],
                value='aaa',
                style={"width": 240}
            )
        ]
                    
    return make_row([
            make_column(12, children)
            ])

sidebar_header = dbc.Row(
    [
        dbc.Col(html.H5("      ", className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.9)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        # use the Collapse component to animate hiding / revealing links
        html.Br(),
        dbc.Collapse(
            dbc.Nav(
                [
                    html.Button(
                        id= "csv-dashboard-data-vis",
                        children=[
                            html.I(className="fas fa-envelope-open-text mr-2"),
                            html.Span("Data Visualization")
                        ], 
                        style ={
                            "border": "none",
                            "textAlign": "left",
                            "background": "#ebe6e6",
                            "fontSize": "1.3rem",
                            "marginTop": 10
                        }
                    ),
                    html.Button(
                        id= "csv-dashboard-sql-tool",
                        children=[
                            html.I(className="fas fa-envelope-open-text mr-2"),
                            html.Span("SQL Tool")
                        ], 
                        style ={
                            "border": "none",
                            "textAlign": "left",
                            "background": "#ebe6e6",
                            "fontSize": "1.3rem",
                            "marginTop": 10
                        }
                    ),
                    html.Button(
                        id = "csv-dashboard-var-list",
                        children=[
                            html.I(className="fas fa-envelope-open-text mr-2"),
                            html.Span("Variable Lists"),
                        ],
                        style ={
                            "border": "none",
                            "textAlign": "left",
                            "background": "#ebe6e6",
                            "fontSize": "1.3rem",
                            "marginTop": 10
                        }
                    ),
                    html.Button(
                        id="csv-dashboard-models",
                        children =[
                            html.I(className="fas fa-envelope-open-text mr-2"),
                            html.Span("Models")
                        ],
                        style ={
                            "border": "none",
                            "textAlign": "left",
                            "background": "#ebe6e6",
                            "fontSize": "1.3rem",
                            "marginTop": 10
                        }
                    )
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse"
        ),
    ],
    id="sidebar",
)

def csv_dashboard():
    """
    uppermost layout of csv_dashboard page
    """ 
    children=[
        sidebar,
        html.Div(id="page-content", className="content")
    ]

    return children