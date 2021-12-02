# import of internal modules
from utils import make_toast, return_box

# import of external libraries
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from gridlayout import GridLayout

def home():
    """
    uppermost layout of home page
    """ 


    children2= dbc.Tabs(
        [
            dbc.Tab(    
                children=[
                    html.Div(
                        children=["content test "],
                        style={"padding": 10}
                    ),
                    html.Div(
                        children=["content test "],
                        style={"padding": 10}
                    ),
                    html.Div(
                        children=["content test "],
                        style={"padding": 10}
                    ),
                    html.Div(
                        children=["content test "],
                        style={"padding": 10}
                    ),
                    html.Div(
                        children=["content test "],
                        style={"padding": 10}
                    ),
                    html.Div(
                        children=["content test "],
                        style={"padding": 10}
                    )
                ], 
                label="Tab 1"
            ),
            dbc.Tab("kk2", label="Tab 2"),
        ]
    )
    children=[
            html.Br(),
            html.Div([html.Button(id="button-to-csv-select", children="Upload .csv and go to interactive dashboard", n_clicks=0)],style={"textAlign": "center"}),
            html.Br()        
            #html.Div([html.Button(id="change-page-button", children="", n_clicks=0)],style={"display": "none"})
        ]
        
    return children