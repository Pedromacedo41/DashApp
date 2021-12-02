# import main app object for callback registration
from app import app 

# import of internal modules
from pages.select_csv.layout import select_csv
from pages.text_extraction.layout import pdf_upload, bilag
from pages.csv_dashboard.layout import csv_dashboard, build_tabs, tab1, tab2, build_variab_list, data_vis, sql_tool
from pages.csv_review.layout import csv_review
from pages.text_extraction.layout import text_extraction
from pages.home.layout import home
from dash_extensions.enrich import ServersideOutput
from dash_extensions.enrich import Trigger


# import of external libraries
import dash
import json
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State, ALL
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


# responsable for page display, session and go back button visibility in top pannel
"""
@app.callback(Output("app-container", "children"),
              Output("app-container", "style"),
              Output("go-back", "style"),
              Input("page", "data"))
def app_container(page, data):
    if(page=="home"):
        return home(), {"width": "100%", "padding": 70}, {"display": "None"}

    if(page=="select_csv"):
        return select_csv(), {"width": "70%", "padding": 70}, {}

    if(page == "csv_dashboard"):
        return csv_dashboard(), {"width": "100%", "padding": 0}, {}

    if(page == "text_extraction"):
        return text_extraction(), {"width": "100%", "padding": 0}, {}

    return html.P("not implemented"), {"width": "40%", "padding": 70}, {}
"""

@app.callback(Output("app-container", "children"),
              Output("app-container", "style"),
              Output("go-back", "style"),
              Output("session-div", "style"),
              Output("page", "data"),
              Input({'type': "select-csv-edit-buttom", 'index': ALL}, 'n_clicks'),
              #Input("go-back", "n_clicks"),
              #Input("button-to-csv-select", "n_clicks"),
              #State("page", "data"),
              State("data_df", "data"))
def app_container(click_values, data_df):
    
    ctx = dash.callback_context
    if ctx.triggered:
        prop_id = ctx.triggered[0]['prop_id'].split('.')[0]   
        dic = json.loads(prop_id)
        idx = int(dic["index"])

        if(ctx.triggered[0]['value'] >0):
            return csv_review(data_df[idx]), {"width": "100%", "padding": 20}, {}, {"display": "none"}, "csv_review"
        
        else:
            return dash.no_update

    return dash.no_update


@app.callback(Output("app-container", "children"),
              Output("app-container", "style"),
              Output("go-back", "style"),
              Output("session-div", "style"),
              Output("page", "data"),
              Input("button-to-csv-select", "n_clicks"))
def call(n_clicks):
    if(n_clicks>0):
        return select_csv(), {"width": "70%", "padding": 70}, {}, {"display": "none"}, "select_csv"

    return dash.no_update


@app.callback(Output("app-container", "children"),
              Output("app-container", "style"),
              Output("go-back", "style"),
              Output("session-div", "style"),
              Output("page", "data"),
              Input("change-page-button-select-csv", "n_clicks"))
def call(n_clicks):
    if(n_clicks>0):
        return csv_dashboard(), {"width": "100%", "padding": 0}, {}, {}, "csv_dashboard"

    return dash.no_update


@app.callback(Output("app-container", "children"),
              Output("app-container", "style"),
              Output("go-back", "style"),
              Output("session-div", "style"),
              Output("page", "data"),
              Trigger("go-back", "n_clicks"),
              State("page", "data"))
def call(page):
    if(page=="select_csv"):
        return home(), {"width": "100%", "padding": 70}, {"display": "None"}, {"display": "none"}, "home"

    if(page=="csv_review"):
        return select_csv(), {"width": "70%", "padding": 70}, {}, {"display": "none"}, "select_csv"

    if(page=="csv_dashboard"):
        return select_csv(), {"width": "100%", "padding": 20}, {}, {"display": "none"}, "select_csv"

    return dash.no_update


"""
# go back button behavior dependent on page context
@app.callback(
              Output("app-container", "children"),
              Output("app-container", "style"),
              Output("go-back", "style"),
              Output("page", "data"),
              Trigger("go-back", "n_clicks"),
              State("page", "data"))
def app_container(page):
    if(page =="csv_review"):
        return  [home()], {"width": "100%", "padding": 70}, {}, "home"
"""


@app.callback(Output("page-content", "children"), 
              Trigger("csv-dashboard-var-list", "n_clicks"),
              State("page", "data"),
              State("data_df", "data"))
def app_container(page, data):
    if(page == "csv_dashboard"):
        return build_variab_list()


@app.callback(Output("page-content", "children"), 
              Trigger("csv-dashboard-data-vis", "n_clicks"),
              State("page", "data"),
              State("data_df", "data"))
def app_container(page, data):
    if(page == "csv_dashboard"):
        return [data_vis(data)]

@app.callback(Output("page-content", "children"), 
              Trigger("csv-dashboard-regression", "n_clicks"),
              State("page", "data"),
              State("data_df", "data"))
def app_container(page, data):
    if(page == "csv_dashboard"):
        return  [build_tabs(data)]


@app.callback(Output("page-content", "children"), 
              Trigger("csv-dashboard-sql-tool", "n_clicks"),
              State("page", "data"),
              State("data_df", "data"))
def app_container(page, data):
    if(page == "csv_dashboard"):
        return  sql_tool(data)
    
"""
# change page for home page
@app.callback(Output("page", "data"),
              Trigger("button-to-csv-select", "n_clicks"),
              prevent_initial_call=True)
def change_state():
    ctx = dash.callback_context
    if ctx.triggered:
        prop_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if prop_id == "button-to-csv-select":
            return "select_csv"
        elif prop_id == "button-to-text-extraction":
            return "text_extraction"
        else:
            return "some_page"
"""



"""
#change page for select_csv page
@app.callback(Output("page", "data"),
              Trigger("change-page-button-select-csv", "n_clicks"),
              prevent_initial_call=True)
def change_state():
    return "csv_review"
"""

"""
#change page for csv_review page
@app.callback(Output("page", "data"),
              Trigger("change-page-button-csv-review", "n_clicks"),
              prevent_initial_call=True)
def change_state():
    return "csv_dashboard"
"""


###############################
#    side bar routing         #
###############################

"""
@app.callback(
    Output("page-content", "children"), 
    Input("url", "pathname"),
    State("page", "data"),
    State("data_df", "data"))
def render_page_content(pathname, page, data):
    if(page=="csv_dashboard"):
        if pathname == "/data-vis":
            return [data_vis(data)]
        if pathname == "/variable-list-creation":
            return build_variab_list()
        elif pathname == "/regression":
            return  [build_tabs(data)]
        # If the user tries to reach a different page, return a 404 message

    elif(page=="text_extraction"):
        if pathname == "/pdfupload":
            return pdf_upload()
        elif pathname == "/bilag":
            return bilag(None)

    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
"""


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""