# import main app object for callback registration
from app import app 
from app import fsc

# import of internal modules
from utils import log, make_toast

# import of external libraries
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State,  ALL, MATCH
import dash_html_components as html
from dash_extensions.enrich import ServersideOutput, Trigger
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash_extensions.snippets import send_data_frame

import base64
import json
import io
import pandas as pd

import re
import dash


##########################
#  Callbacks section     #
##########################


# upload csv button
@app.callback(ServersideOutput("data_df", "data"),                   # global scope (csv_review and csv_dashboard pages)
              #Output("fancy_list_edit", "children"),
              Input("upload-data", "contents"),
              Input("select-csv-clear-all", "n_clicks"),
              Input({'type': "select-csv-delete-buttom", 'index': ALL}, 'n_clicks'),
              State("upload-data", "filename"),
              State("upload-data", "last_modified"),
              State("session-id", "data"),
              State("data_df", "data"),  
              prevent_initial_call=True,
              memoize=True
              #State("fancy_list_edit", "children"),
)                 
def update_output(contents, delete_click, click_values, filenames, date, session_id, data_df):
    """
    read csv and store it as json in 'data' object (browser memory)

    :param content: base64 string with csv content
    :param name: name of file
    :param date: file date
    :param session_id: user session id for app logging

    :return: tuple containing html component with csv summary information; dataframe as json object (supported format for sharing data across callbacks)
    """ 

    ctx = dash.callback_context
    if ctx.triggered:
        prop_id = ctx.triggered[0]['prop_id'].split('.')[0]   
        if(prop_id == "upload-data"):
            if(contents is not None):
                #data_df2 = data_df.copy()
                fsc.set("message-progress", "Starting")  # update progress
                fsc.set("progress", "0")  # update progress
                for i, content in enumerate(contents):
                    fsc.set("message-progress", "Analysing file "+ str(i+1) + "/"+ str(len(contents))+ " : " + filenames[i] + " ...")  # update progress
                    fsc.set("progress", str((i) / len(contents)))  # update progress
                    data_df.append(parse_contents(content, filenames[i], date, session_id))
                    fsc.set("progress", str((i + 1) / len(contents)))  # update progress
                return data_df

            else:
                if(data_df is None):
                    return []
                else:
                    return data_df

        elif prop_id == "select-csv-clear-all":
            return []

        else:   
            dic = json.loads(prop_id)
            idx = int(dic["index"])
            #data_df2 = data_df.copy()
            data_df.pop(idx)
            return data_df
            
@app.callback(Output("progress", "children"), Output("progress", "value"), Output("message-progress-div", "children"), Trigger("select-csv-interval", "n_intervals"))
def update_progress():
    value = fsc.get("progress")  # get progress
    if value is None:
        raise PreventUpdate

    else:
        value2 = float(fsc.get("progress")) * 100
        if(value2 == 100):
            return "{:.0f}%".format(float(fsc.get("progress")) * 100), float(fsc.get("progress")) * 100, "Finished."
        else:
            return "{:.0f}%".format(float(fsc.get("progress")) * 100), float(fsc.get("progress")) * 100, fsc.get("message-progress")

# upload csv button
@app.callback(Output("select-csv-download", "data"),
              Input({'type': "select-csv-download-buttom", 'index': ALL}, 'n_clicks'),
              State("data_df", "data"),  
              State("custom_data_session", "data"),
              prevent_initial_call=True 
              #State("fancy_list_edit", "children"),
)                 
def update_output(click_values, data_df, session):
    """
    read csv and store it as json in 'data' object (browser memory)

    :param content: base64 string with csv content
    :param name: name of file
    :param date: file date
    :param session_id: user session id for app logging

    :return: tuple containing html component with csv summary information; dataframe as json object (supported format for sharing data across callbacks)
    """ 

    ctx = dash.callback_context
    if ctx.triggered:
        if(ctx.triggered[0]['value']>0):
            prop_id = ctx.triggered[0]['prop_id'].split('.')[0]   
            
            dic = json.loads(prop_id)
            idx = int(dic["index"])
            df = data_df[idx]
            return send_data_frame(df.to_csv, session["filenames"][idx]+ "_edited")
        else:
            return dash.no_update

    return dash.no_update


"""
# upload .json button
@app.callback(ServersideOutput("var-list", "data"),     # global scope
              Input("upload-data2", "contents"),      
              State("upload-data2", "filename"),
              State("upload-data2", "last_modified"),
              State("session-id", "data"),               # global scope
              State("page", "data"))                # global scope
def update_output_2(content,name, date,  session_id, page):
    
    parses an encoded json file to a python dict

    :param content: base64 string with csv content
    :param filename: name of file
    :param date: file date
    :param session_id: user session id for app logging
    :param page: current page
    
    :return: pythin dict object with session information to a callback-shared object (custom-data-session)
    
    print("parse json")
    if(content is not None):
        return parse_contents_json(content, name, date, session_id, page)
    else:
        return None



# notifications after .json upload
@app.callback(Output("output-data-upload2", "children"),
              Input("var-list", "data"),      # global scope 
              State("upload-data2", "filename"),
              State("session-id", "data"),               # global scope
              State("page", "data"))                # global scope
def upload_div_info(session_data,filename, session_id, page):
    
    notification of json containing session information parsing and validation

    :param session_data: python dict with parsed json (feeded by update_output_2 callback)
    :param filename: name of session file
    :param session_id: user session id for app logging
    :param page: current page
    
    :return:   html component after session upload button and toast notification
    
    if page!="select_csv":
        raise PreventUpdate
    else:
        if(filename is not None):
            if False: 
                return [
                        html.Div([html.H5(filename, style={'fontSize':14, 'paddingLeft': 20})]),
                        make_toast("Invalid Session File","Please provide a valid session file" ,"danger", 2000, is_open=True)
                ]
            else:
                return [
                        html.Div([html.H5(filename, style={'fontSize':14, 'paddingLeft': 20})]),
                        make_toast("Valid Session File","Valid session file" ,"success", 2000, is_open=True)
                ]
"""

"""
@app.callback(Output("notification-submit-csv", "is_open"),
              Input("change-page-button", "n_clicks"),
              State("page", "data"),
              State("data", "data"),
              prevent_initial_call=True)
def notification_missing_csv(n_clicks, page, data):
    
    validation of csv upload before proceeding to csv_review page

    :param n_clicks: how many times button was clicked
    :param page: current page
    :param data: parsed dataframe from csv

    :return: boolean indicating if toast must be displayed
    
    if(n_clicks==0):
        raise PreventUpdate
    else:
        if(page=="select_csv"):
            if(data is None):
                return True
            else:
                raise PreventUpdate
        else:
            raise PreventUpdate

@app.callback(
    ServersideOutput("data_df", "data"),
    Input("change-page-button", "n_clicks"),
    #Input({'type': "select-csv-delete-buttom", 'index': ALL}, 'n_clicks'),
    State("data_df", "data"),
    prevent_initial_update=True
)
def show_columns(n_clicks,data_dict):
    if(n_clicks>0):
        return data_dict
    else:
        raise dash.no_update
  
    #ctx = dash.callback_context
    #if ctx.triggered:
        idx = int(json.loads(ctx.triggered[0]['prop_id'].split('.')[0])["index"])
        if(ctx.triggered[0]['value'] > 0):
            print("jjjj1")
            #data_dict2 = data_dict.copy()   
            #data_dict2.pop("T"+str(idx))
            #print(data_dict2)
            return data_dict
        else:
            print(data_dict)
            return data_dict
    else:
        print(data_dict)
        return data_dict
"""


@app.callback(
    ServersideOutput("custom_data_session", "data"),
    Input("upload-data", "filename"),
    Input("select-csv-clear-all", "n_clicks"),
    Input({'type': "select-csv-delete-buttom", 'index': ALL}, 'n_clicks'),
    Input({'type': "select-csv-edit-buttom", 'index': ALL}, 'n_clicks'),
    State({'type': "textarea-proxyname-select-csv", 'index': ALL}, 'value'),
    State("custom_data_session", "data"),
    prevent_initial_update=True
)
def show_columns(filenames, delete_click, click_values, click_edit_values , names_values, session):
    ctx = dash.callback_context
    if ctx.triggered:
        prop_id = ctx.triggered[0]['prop_id'].split('.')[0]   
        session2 = session.copy()
        if(prop_id == "upload-data"):
            if "filenames" not in session2:
                if(filenames is not None):
                    session2["filenames"] = filenames
                else:
                    session2["filenames"] = []
            else:
                my_list = session2["filenames"].copy()
                if(filenames is not None):
                    my_list.extend(filenames)
                session2["filenames"] = my_list

            return session2

        elif prop_id == "select-csv-clear-all":
            if "filenames" in session2:
                session2["filenames"]=[]
            if "proxy_names" in session2:   
                session2.pop("proxy_names") 

            return session2
            
        else:
            dic = json.loads(prop_id)
            mul_prop_id = dic["type"]

            if mul_prop_id == "select-csv-delete-buttom":
                idx = int(dic["index"])
                my_list = session2["filenames"].copy()

                #print(ctx.triggered[0]["value"])
                if ctx.triggered[0]["value"] >0 :
                    my_list.pop(idx)

                session2["filenames"] = my_list

                return session2

            if mul_prop_id == "select-csv-edit-buttom":
                session2["proxy_names"] = names_values
                return session2


    return dash.no_update

            

@app.callback(
    Output("fancy_list_edit", "children"),
    Input("data_df", "data"),
    Input("custom_data_session", "data"),
    prevent_initial_update=True
)
def show_columns(data_df, session):
    print("printing list")
    #print(data_dict)
    children2 = []
    if data_df is not None:
        for i, df in enumerate(data_df):
            buffer = io.StringIO()
            df.info(memory_usage='deep',buf=buffer, show_counts= False, max_cols=5)
            s = buffer.getvalue()
            #print(session["filenames"])
            elem = html.Div(
                    className="twelve columns",
                    children=[
                        html.Div(
                            className="two columns",
                            children= [
                                session["filenames"][i]
                            ]
                        ),
                        html.Div(
                            className="one columns",
                            children= [
                                "{:.1f}".format(df.memory_usage(deep=True).sum()/1024/1024)
                            ]
                    ),
                    html.Div(
                        className="two columns",
                        children=[
                            dcc.Textarea(
                                id={"type": 'textarea-proxyname-select-csv',
                                    "index": i
                                },
                                value=  session["proxy_names"][i] if "proxy_names" in session else re.sub(r'[ ]', "_", session["filenames"][i].split(".")[0]),
                                style={"background": "white",
                                       "color": "black",
                                       "width": "100%", "fontSize": 12, "height":10}
                            )
                        ]
                    ),
                    html.Div(
                        className="three columns",
                        children=[
                            dcc.Textarea(
                                id={"type": 'textarea-info-select-csv',
                                    "index": i
                                },
                                value=s,
                                disabled=True,
                                style={"background": "white", "color": "black", "width": "100%", "fontSize": 12, "height":20}, 
                            )
                        ]
                    ),
                    html.Div(
                        className="two columns",
                        children=[
                            dcc.Textarea(
                                id={"type": 'textarea-failed-select-csv',
                                    "index": i
                                },
                                value=  str(list(df.select_dtypes(include="object").columns)),
                                disabled=True,
                                style={"background": "white", "color": "black", "width": "100%", "fontSize": 12, "height":20}, 
                            )
                        ]
                        #style = {'display': 'inline-block', "marginBottom": -12, "width":300, "marginLeft": 180}  
                    ),
                    html.Div(
                        className="two columns",
                        children=[
                            html.Div(
                                dbc.Button(
                                    id={"type": "select-csv-delete-buttom",
                                        "index": i
                                    },
                                    children=[html.I(className="fas fa-trash mr-2", style={})],
                                    n_clicks=0,
                                    color="primary",
                                    style={"fontSize":"1.6rem","background": "none","border": "none", "marginBottom": 8, "marginRight":0}
                                ), 
                                
                                style={'display': 'inline-block'}
                            ),
                            html.Div(
                                dbc.Button(
                                    id={"type": "select-csv-edit-buttom",
                                        "index": i
                                    },
                                    children=[html.I(className="fas fa-edit mr-2", style={})],
                                    n_clicks=0,
                                    color="primary",
                                    style={"fontSize":"1.6rem","background": "none","border": "none", "marginBottom": 8, "marginRight":0}
                                ), 
                                style={'display': 'inline-block'} 
                            ),
                            html.Div(
                                dbc.Button(
                                    id={"type": "select-csv-download-buttom",
                                        "index": i
                                    },
                                    children=[html.I(className="fas fa-download mr-2", style={})],
                                    n_clicks=0,
                                    color="primary",
                                    style={"fontSize":"1.6rem","background": "none","border": "none", "marginBottom": 8, "marginRight":0}
                                ), 
                                style={'display': 'inline-block'} 
                            )
                        ],
                        style={"justifyContent": "right"}
                    )
                ]
            )

            children2.append(elem)
    
    return children2

    



##########################
#  Auxiliar functions    #
##########################

def parse_contents(content, filename, date, session_id):
    """
    parses an encoded csv file to a pandas object

    :param content: base64 string with csv content
    :param filename: name of file
    :param date: file date
    :param session_id: user session id for app logging

    :return: tuple containing html component with csv summary information; dataframe as json object (supported format for sharing data across callbacks)
    """ 

    content_type, content_string = content.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            log(session_id, "Successful .csv upload")

    except Exception as e:
        log(session_id, "Error processing .csv upload")
        log(session_id, e)
        return None

    return df



def parse_contents_json(contents, filename, date, session_id, page):
    """
    parses an encoded json file to a python dict

    :param content: base64 string with csv content
    :param filename: name of file
    :param date: file date
    :param session_id: user session id for app logging
    :param page: current page

    :return: pythin dict object with session information
    """ 
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'json' in filename:
            # Assume that the user uploaded a CSV file
            obj = json.loads(decoded)

    except Exception as e:
        log(session_id, "Error processing .json upload")
        log(session_id, e)
        return {"status": 0}

    return obj


def dict_check(obj, page):
    """
    validation of a .json session file

    :param obj: python dict 
    :param page: current page
    :return: boolean with validation status
    """ 
    list_of_ids = ["demo-dropdown-value"]
    
    for a in list_of_ids:
        if a not in obj:
            return False

    return True