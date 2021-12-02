# import of internal modules
from utils import make_toast

# import of external libraries
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_extensions import Download

markdown_text = '''
### `*` Data Upload (.csv):

'''

markdown_text2 = '''
### Upload session file (.json)

'''

markdown_text3 = '''
##### Options
'''

def select_csv():
    """
    uppermost layout of select_csv page
    """ 
    children=[
            dcc.Markdown(children=markdown_text),
            html.Br(),
            dcc.Upload(
                id="upload-data",
                accept= ".csv",
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select files', style={"color": "#87CEFA"})
                ]),
                style={
                    'width': '90%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px',
                },
                # Allow multiple files to be uploaded
                multiple=True
            ),
            html.Div(id= "message-progress-div", style={"paddingLeft": 35}),
            html.Br(),
            html.Div(
                children=[
                        dbc.Progress(
                            id="progress", 
                            value=75, 
                            striped=True, 
                            children="25 %",
                            color = "#3d5b7b",
                            style = {"fontSize": 14, "fontWeight": 500, "width": "100%", "height": "2rem"}
                        )
                ],
                style= {"width": "90%", "paddingLeft": 10}
            ),
            dcc.Interval(id="select-csv-interval", interval=1000),
            html.Br(),
            html.Div(
                dbc.Button(
                    id="select-csv-clear-all",
                    children="Delete all tables",
                    n_clicks=0,
                ),
                style={"textAlign": "center"}       
            ),
            html.Br(),
            html.Div(
                className="twelve columns",
                children=[
                    html.Div(
                        className="two columns",
                        children=[dbc.Label("Filename", style={"fontSize": 13})]
                    ),
                    html.Div(
                        className="one columns",
                        children=[dbc.Label("Size", style={"fontSize": 13})]
                    ),
                     html.Div(
                        className="two columns",
                        children=[dbc.Label("Name (editable)", style={"fontSize": 13})]
                    ),
                    html.Div(
                        className="three columns",
                        children=[dbc.Label("Summary", style={"fontSize": 13})]
                    ),
                    html.Div(
                        className="two columns",
                        children=[dbc.Label("Failed Columns", style={"fontSize": 13})]
                    ),
                    html.Div(
                        className="two columns",
                        children=[dbc.Label("Options", style={"fontSize": 13})]
                    )
                ],
                style= {"paddingLeft": 30, 'width': '90%'}
            ),
            html.Hr(style={"borderTop": "0.1px solid #000", "marginBottom": "1.5rem", "paddingLeft": 30}),
            dbc.Spinner(
                children=
                    [html.Div(
                        id="fancy_list_edit",
                        style= {"paddingLeft": 30, 'width': '90%'}
                    )],
                spinner_style={"width": "3rem", "height": "3rem"}
            ),
            Download("select-csv-download"),
            html.Br(),
            html.Br(),
            dcc.Markdown(children=markdown_text2, style= {"paddingLeft": 10, 'width': '90%', "marginTop": 90}),
            html.Br(),
            dcc.Upload(
                id="upload-data2",
                accept= ".json",
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files', style={"color": "#87CEFA"})
                ]),
                style={
                    'width': '90%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px',
                },
                # Allow multiple files to be uploaded
                multiple=False
            ),
            html.Div(id="output-data-upload2", style={"fontsize":10}),
            html.Br(),
            html.Br(),
            html.Div([
                    html.Button(id="change-page-button-select-csv", children="SUBMIT", n_clicks=0),
                    make_toast("Missing .csv","Please provide a .csv file" ,"danger", 2000, triggering_id="notification-submit-csv")
                ],
                style={"textAlign": "center"})
        ]
        
    return children
