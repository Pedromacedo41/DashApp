# import main app object for asset 
from app import app 

# import of external libraries
import dash_core_components as dcc
import dash_html_components as html
import uuid

from pages.home.layout import home
from utils import build_banner, generate_modal

def serve_layout():
    session_id = str(uuid.uuid4())
    return html.Div(
        id="big-app-container",
        children=[
            dcc.Store(data=session_id, id="session-id"),
            dcc.Store(id="data_df", data=[]),
            dcc.Store(id="custom_data_session", data={}),
            dcc.Store(id="page", data="home"),
            build_banner([
                app.get_asset_url("logo_IE3M.png"),
                app.get_asset_url("aphp.gif")
            ]),
            html.Div(
                id="app-container",
                children=home(),
                style= {"width": "100%", "padding": 70}
            ),
            generate_modal()
        ],
    )
