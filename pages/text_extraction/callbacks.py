from app import app 

# import of internal modules
from utils import log, make_toast
from pages.text_extraction.layout import textarea_text_display, pdf_viewer, bilag

# import of external libraries
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from dash_extensions.enrich import ServersideOutput
import dash_html_components as html
import dash_core_components as dcc
import sys, traceback
import pdftotext
from dash_extensions.enrich import Trigger

import base64
import json
import io
import pandas as pd
import numpy as np
import datetime as dt
import dash



##########################
#  Callbacks section     #
########################## 
# upload csv button


@app.callback( 
    ServersideOutput("bilag_table", "data"),
    Trigger("bilag-random-data", "n_clicks"),      
)                 
def random_bilag_atribution():
    time_stamp = dt.datetime.now().timestamp()
    np.random.seed(int(time_stamp))
    print("i was clicked")
    return np.random.choice([0,1,2,3,4], size = 77, p=[0.7, 0.1, 0.1, 0.05, 0.05])


@app.callback(
    Output("page-content", "children"),
    Input("bilag_table", "data"))
def update_vis(table): 
    print("i am hereeee")
    return bilag(table)
    

@app.callback( 
              #ServersideOutput("pdf_parsed", "data"),                   # global scope (csv_review and csv_dashboard pages)
              Output("output-text-upload-pdf-text-extraction1", "children"),
              Output("output-text-upload-pdf-text-extraction2", "children"),
              Output("output-text-upload-pdf-file", "children"),
              Input("upload-pdf-text-extraction-page", "contents"),
              State("upload-pdf-text-extraction-page", "filename"),
              State("upload-pdf-text-extraction-page", "last_modified"),
              State("session-id", "data")
)                 
def update_output(content, name, date, session_id):
    """
    read pdf 

    :param content: base64 string with csv content
    :param name: name of file
    :param date: file date
    :param session_id: user session id for app logging

    :return: tuple containing html component with csv summary information; dataframe as json object (supported format for sharing data across callbacks)
    """ 

    if(content is not None):
        try:
            pdf, column_text, fp = parse_contents(content, name, date, session_id)
            return textarea_text_display(" ".join(column_text)), textarea_text_display("\n\n".join(pdf)), pdf_viewer(content)
        except:
            traceback.print_tb(*sys.exc_info())
            return [html.P("Parse Error")], [html.P("Parser Error")], [html.P("Parser Error")]
    else:
        return [html.P("No data")], [html.P("No data")], [html.P("No data")]



##########################
#  Auxiliar functions    #
##########################
def parse_contents(content, filename, date, session_id):
    """
    parses an encoded pdf file

    :param content: base64 string with csv content
    :param filename: name of file
    :param date: file date
    :param session_id: user session id for app logging

    :return: tuple containing html component with csv summary information; dataframe as json object (supported format for sharing data across callbacks)
    """ 

    content_type, content_string = content.split(',')
    decoded = base64.b64decode(content_string)

    if 'pdf' in filename:
        with io.BytesIO(decoded) as fp:
            pdf = pdftotext.PDF(fp)
            return pdf, extract_columns_from_pdf(pdf), fp

    return None, None, None


def extract_columns_from_pdf(pdf):
    text_column1 = []
    text_column2 = []

    for i in range(len(pdf)):
        for phrase in pdf[i].split("\n"):
            pre_split = phrase.split("  ")
            #print(pre_split)
            try:
                pre_split[pre_split.index("")]= "***"
            except:
                pre_split.append("***")
            split = [a for a in pre_split if a != '']

            a = split.index("***")
            if(a==0):
                if len(split) >1 :
                    text_column2.append(split[1])
                else:
                    # newline for both columns
                    text_column1.append("\n")
                    text_column2.append("\n")

            else:
                if(a==1):
                    if(len(split)==3):
                        text_column1.append(split[0])
                        text_column2.append(split[2])
                    else:
                        text_column1.append(split[0])
                        text_column2.append("\n")
    
    return text_column2

