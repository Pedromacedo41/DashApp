# import of external libraries
import pathlib

import dash
import dash_auth
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_extensions.enrich import DashProxy, TriggerTransform, MultiplexerTransform, ServersideOutputTransform, NoOutputTransform, FileSystemCache

"""
app = DashProxy(transforms=[
    TriggerTransform(),  # enable use of Trigger objects
    MultiplexerTransform(),  # makes it possible to target an output multiple times in callbacks
    ServersideOutputTransform(),  # enable use of ServersideOutput objects
    NoOutputTransform(),  # enable callbacks without output
])
"""

fsc = FileSystemCache("cache_dir")
fsc.set("progress", None)
fsc.set("message-progress", "")


##################################
#    App  general settings       #
##################################
proxy_wrapper_map = {Output("log0", "children"): lambda proxy: dcc.Loading(proxy, type="dot")}

app = DashProxy(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}], 
    external_scripts=[
        'https://oss.sheetjs.com/sheetjs/xlsx.full.min.js'
    ],
    external_stylesheets=[
        dbc.themes.BOOTSTRAP, 
        "https://use.fontawesome.com/releases/v5.15.1/css/all.css",
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    ],
    suppress_callback_exceptions=True,
    transforms=[
        TriggerTransform(),  # enable use of Trigger objects
        MultiplexerTransform(proxy_wrapper_map),  # makes it possible to target an output multiple times in callbacks
        ServersideOutputTransform(),  # enable use of ServersideOutput objects
        #NoOutputTransform() # enable callbacks without output
    ]
)


app.title = "Exploratory Data Analysis"
server = app.server

VALID_USERNAME_PASSWORD_PAIRS = [
    ['hell', 'wod']
]
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


APP_PATH = str(pathlib.Path(__file__).parent.resolve())

