
# import of external libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_daq as daq

import logging

def log(userid, message):
    """
    logs user activity in system journal   

    :param user_id: user session id 
    :param message: message
    """
    print(userid + ": " + message)
    logging.info(userid + ": " + message)
    



def return_box(title, content, idx, has_delete= False, has_expand=True):
    return html.Div(
            className="shadowsharp",
            children=[
                html.Div(
                    children= [
                        html.Div(
                            children=[
                                dbc.Label(title, style={'display': 'inline-block', "fontWeight": 1000, "paddingRight": 20}),
                                dbc.Button(
                                    className="expand",
                                    id={
                                        'type': 'info-button',
                                        'index': idx
                                    },
                                    children=[html.I(className="fas fa-info", style={})],
                                    n_clicks=0,
                                    color="primary",
                                    style={"fontSize":"1.4rem",
                                          "background": "none",
                                          "border": "none", 
                                          'display': 'inline-block',
                                           "marginTop": -4, "padding":0}
                                ), 
                                dbc.Button(
                                    className="expand",
                                    id={
                                        'type': 'clone-button',
                                        'index': idx
                                    },
                                    children=[html.I(className="fas fa-clone", style={})],
                                    n_clicks=0,
                                    color="primary",
                                    style={"fontSize":"1.4rem",
                                          "background": "none",
                                          "border": "none", 
                                          'display': 'inline-block',
                                           "marginTop": -4, "padding":0}
                                ), 
                                dbc.Button(
                                    className="expand",
                                    id={
                                        'type': 'delete-button',
                                        'index': idx
                                    },
                                    children=[html.I(className="fas fa-trash-alt mr-2", style={})],
                                    n_clicks=0,
                                    color="primary",
                                    style={"fontSize":"1.4rem",
                                          "background": "none",
                                          "border": "none", 
                                          'display': 'inline-block' if has_delete else 'none', 
                                           "marginTop": -4, "padding":0}
                                ), 
                                dbc.Button(
                                    className="expand",
                                    id={
                                        'type': 'collapse-button',
                                        'index': idx
                                    },
                                    children=[html.I(className="fas fa-expand-alt mr-2", style={})],
                                    n_clicks=0,
                                    color="primary",
                                    style={"fontSize":"1.4rem",
                                           "background": "none",
                                           "border": "none", 
                                           'display': 'inline-block' if has_expand else 'none',
                                           "marginTop": -4, 
                                           "padding":0}
                                ) 
                            ],
                            style={"textAlign": "right", "width":"100%", "position": "absolute", "z-index":1, "x":"50%"}
                        ),
                        dbc.Collapse(
                            content,
                            id={
                                'type': 'collapse-home',
                                'index': idx
                            },
                            is_open=True,
                            style={"height":"100%"}
                        )
                    ]
                )
            ],
            style={"backgroundColor": "white", "padding": 8, "minHeight": 10, "height": "100%"}
        )

############################
#    Layout functions      #
############################

def build_banner(logo_list):
     """
     banner component (page header)
     """

     children=[
            
            html.Button(
                id="go-back", children=["GO back"], n_clicks=0, style={"display": "none"}
            ),
            html.Div(
                id="session-div", 
                children=[
                    html.Button("SAVE SESSION", id="save-session-button", n_clicks=0),
                    dcc.Download(id="download-session")
                ],
                style={"display": "none"}
            ),
            html.Div(
                children=[
                    html.Button(
                        id="learn-more-button", children=["LEARN MORE"], n_clicks=0, style={"paddingRight":20}
                    )
                ],
                style={"paddingRight": 50}
            )
            #dbc.Label("Dark Theme", style={"paddingRight": 10, "paddingLeft": 20}),
            #daq.BooleanSwitch(
            #    id='theme_switch',
            #    on=False,
            #    #color="#46496EE3",
            #    style={"paddingRight":20}
            #)
     ]

     children.extend([html.Img(src=a) for a in logo_list])

     return html.Div(
               id="banner",
               className="banner",
               children=[
                    html.Div(
                         id="banner-text",
                         children=[
                              html.H5(""),
                         ],
                    ),
                    html.Div(
                         id="banner-logo",
                         children=children
                    )
               ]
     )



def generate_section_banner(title):
    return html.Div(className="section-banner", children=title)


def make_big_tab(title, my_id):
     """
     create a big tab element (uppermost tab whitin a page)

     :param title: tab title
     :param my_id: tab id
     """
     return dcc.Tab(id=my_id, 
                   label=title,
                   value=my_id,
                   className="custom-tab",
                   selected_style= { 
                       "background-color": "#161a28",
                       "letter-spacing": "1px",
                       "color": "inherit",
                       "border": 0,
                       "border-bottom": "#1E2130 solid 4px !important",
                       "display": "flex",
                       "flex-direction": "column",
                       "align-items": "center",
                       "justify-content": "center",
                       "cursor": "pointer",
                       "height": "18px",
                       "border-bottom": "#91dfd2 solid 4px !important"
                    },
                   selected_className="custom-tab--selected",
                   style= {
                       "background-color": "#161a28",
                       "letter-spacing": "1px",
                       "color": "inherit",
                       "border": 0,
                       "border-bottom": "#1E2130 solid 4px !important",
                       "display": "flex",
                       "flex-direction": "column",
                       "align-items": "center",
                       "justify-content": "center",
                       "cursor": "pointer",
                       "height": "18px"
                   }
            )


def make_mini_tab(tab_content, label):
    return dbc.Tab(dbc.Spinner(tab_content), label=label, active_tab_style ={"background-color": "#000"})



def make_column(width, children, title=None, border_left = False):
    classnames = ["one columns", "two columns", "three columns", "four columns", "five columns", "six columns",
                  "seven columns", "eight columns", "nine columns", "ten columns", "eleven columns", "twelve columns"]

    className = classnames[width-1]
    if border_left:
        style = { "height": "100%", 
                  "flex": "1 1 auto", 
                  "margin": 0, 
                  #"border-left": "#1E2130 solid 0.8rem"
                  "border-left": "#fff solid 0.8rem"
                }
    else:
        style = { "height": "100%", 
                  "flex": "1 1 auto"}

    if(title is not None):
        return html.Div(
                style = style,
                className=className,
                children=[
                    generate_section_banner(title),
                    html.Div(style={"padding": "1rem 2rem 1rem 1rem"}, children= children)
                ])
    else:
        return html.Div(
                style = style,
                className=className,
                children=[
                    html.Div(style={"padding": "1rem 2rem 1rem 1rem"}, children= children)
                ])


def make_row(children):
    return html.Div(
        children= [
            html.Div(
                id= "top-section-container2",
                style = {"width": "100%", 
                         "max-width": "100%",
                         "height": "100%",
                         "display": "flex",
                         "flex-direction": "row",
                         "justify-content": "center",
                         #"border-top": "#1E2130 solid 0.8rem",
                         "border-top": "#fff solid 0.8rem",
                         "margin": 0,
                         "padding": 0},
                className="row",
                children=children
            )
        ]
    )

def make_toast(message_header, message_content, type_of_message, duration,  triggering_id= None, inline=False, is_open=False):
     """
     show user notification in the top of screen or alongside the triggering html component (ex: button)

    :param message_header: message title
    :param message_content: message content
    :param type_of_message: color of notification:  "danger" (red), "success" (green), "primary" (blue)
    :param triggering_id: the id of the html component whose input triggers the toast. Toast with triggering_id defined will usually have registered callbacks
    :param inline: whether toast is showed in the top left corner or alongside the triggering component
    :param is_open: if the toast is opened or not
    """

     if(inline):
          style = {"width": 350, 'fontSize':16},
     else:
          style = {"position": "fixed", "top": 66, "right": 10, "width": 350, 'fontSize':16}

     if triggering_id is not None:
          return dbc.Toast(
                    id = triggering_id,
                    header=message_header,
                    is_open = is_open,
                    style=style,
                    icon=type_of_message,
                    dismissable=True,
                    duration=duration,
                         children = [html.P(message_content, className="mb-1")]
               )
     else:
          return dbc.Toast(
                    header=message_header,
                    is_open = is_open,
                    style=style,
                    icon=type_of_message,
                    dismissable=True,
                    duration=duration,
                         children = [html.P(message_content, className="mb-1")]
               )


def generate_modal():
    return html.Div(
        id="markdown",
        className="modal",
        children=(
            html.Div(
                id="markdown-container",
                className="markdown-container",
                children=[
                    html.Div(
                        className="close-container",
                        children=html.Button(
                            "Close",
                            id="markdown_close",
                            n_clicks=0,
                            className="closeButton",
                        ),
                    ),
                    html.Div(
                        className="markdown-text",
                        id= "markdown-text",
                        children=dcc.Markdown(
                            children=(
                                """
                        ###### App Overview

                        texts

                        ###### Quick mannual

                        text

                    """
                            )
                        ),
                    ),
                ],
            )
        ),
    )

          