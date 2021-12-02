# import main app object for callback registration
from app import app 

# import of external libraries
import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import os

import json
    

# ======= Callbacks for modal popup =======
@app.callback(
    Output("markdown", "style"),
    Output("markdown-text", "children"),
    [Input("learn-more-button", "n_clicks"), 
    Input("markdown_close", "n_clicks"),
    State("page", "data")],
)
def update_click_output(button_click, close_click, page):
    ctx = dash.callback_context
    if ctx.triggered:
        prop_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if prop_id == "learn-more-button":
            print(open(os.path.join(".", "pages", page, page + ".md"), "r").read())
            return {"display": "block"}, """  ## Test  """
        
    
    return {"display": "none"}, "## Test"


# ======= Callbacks for modal popup =======
@app.callback(
    Output("theme", "data"),
    Input("theme_switch", "on"),
)
def update_click_output(value):
    if(value):
        return "dark"
    else: 
        return "white"
    

