# import main app object for callback registration
from app import app 

# import of external libraries
import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State, ALL, MATCH
from dash_extensions.enrich import Trigger
import dash_html_components as html

##########################
#  Callbacks section     #
##########################


@app.callback(
    Output({'type': "collapse-home", 'index': MATCH}, "is_open"), 
    [Input({'type': "collapse-button", 'index': MATCH}, "n_clicks")],
    [State({'type': "collapse-home", 'index': MATCH}, "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


