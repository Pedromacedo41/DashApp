# import of external libraries
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

from utils import make_row, make_column, make_mini_tab


sidebar_header = dbc.Row(
    [
        dbc.Col(html.H5("      ", className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        # use the Collapse component to animate hiding / revealing links
        html.Br(),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink([
                        html.I(className="fas fa-envelope-open-text mr-2"),
                        html.Span("Text Extraction"),
                    ], href="/pdfupload", active="exact"),
                    dbc.NavLink([
                        html.I(className="fas fa-envelope-open-text mr-2"),
                        html.Span("Bilag")], href="/bilag", active="exact")
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse"
        ),
    ],
    id="sidebar"
)


def textarea_text_display(text):
    return [dcc.Textarea(
        value=text,
        style={'width': '100%', 'height': "76rem", "fontSize": 13.5, "color": "white", "backgroundColor": "#5a5656"},
    )]

def pdf_viewer(data):
    return [html.Iframe(
        src=data,
        style={'width': '100%', 'height': "80rem"}
    )]


def constitutional(data):
    return [
        html.Br(),
        dbc.Label("Pyrexia – documented > 37,5 ºC"),
        dbc.Label("Weight loss - unintentional > 5 %"),
        dbc.Label("Lymphadenopathy/splenomegaly"),
        dbc.Label("Anorexia")
    ]

def mucocutaneous(data):
    return [
        html.Br(),
        dbc.Label("Skin eruption – severe"),
        dbc.Label("Skin eruption – mild"),
        dbc.Label("Angioedema – severe"),
        dbc.Label("Angioedem – mild"),
        dbc.Label("Mucosal ulceration – severe"),
        dbc.Label("Mucosal ulceration – mild"),
        dbc.Label("Panniculitis/Bullous lupus – severe"),
        dbc.Label("Panniculitis/Bullous lupus – mild"),
        dbc.Label("Major cutaneous vasculitis/thrombosis"),
        dbc.Label("Digital infarcts or nodular vasculitis"),
        dbc.Label("Alopecia – severe16. Alopecia – mild"),
        dbc.Label("Periungual erythema/chilblains"),
        dbc.Label("Splinter haemorrhages")
    ]

def neuropsychiatric(data):
    return [
        html.Br(),
        dbc.Label("Aseptic meningitis"),
        dbc.Label("Cerebral vasculitis"),
        dbc.Label("Demyelinating syndrome"),
        dbc.Label("Myelopathy"),
        dbc.Label("Acute confusional state"),
        dbc.Label("Psychosis"),
        dbc.Label("Acute inflammatory demyelinating polyradiculoneuropathy"),
        dbc.Label("Mononeuropathy (single/multiplex)"),
        dbc.Label("Cranial neuropathy"),
        dbc.Label("Plexopathy"),
        dbc.Label("Polyneuropathy"),
        dbc.Label("Seizure disorder"),
        dbc.Label("Status epilepticus"),
        dbc.Label("Cerebrovascular disease (not due to vasculitis)"),
        dbc.Label("Cognitive dysfunction"),
        dbc.Label("Movement disorder"), 
        dbc.Label("Autonomic disorder"),
        dbc.Label("Cerebellar ataxia (isolated)"),
        dbc.Label("Lupus headache – severe unremitting"),
        dbc.Label("Headache from IC hypertension")
    ]

def muscoloskeletal(data):
    return [
        html.Br(),
        dbc.Label("Myositis – severe"),
        dbc.Label("Myositis – mild"),
        dbc.Label("Arthritis – severe"),
        dbc.Label("Arthritis – moderate/tendonitis/tenosynovitis"),
        dbc.Label("Arthritis – mild/arthralgia/myalgia")
    ]

def cardiorespiratory(data):
    return [
        html.Br(),
        dbc.Label("Myocarditis – mild"),
        dbc.Label("Myocarditis/endocarditis + cardiac failure"),
        dbc.Label("Arrhythmia"),
        dbc.Label("New valvular dysfunction"),
        dbc.Label("Pleurisy/pericarditis"),
        dbc.Label("Cardiac tamponade"),
        dbc.Label("Pleural effusion with dyspnoea"),
        dbc.Label("Pulmonary haemorrhage/vasculitis"),
        dbc.Label("Interstitial alveolitis/pneumonitis"),
        dbc.Label("Shrinking lung syndrome"),
        dbc.Label("Aortitis"),
        dbc.Label("Coronary vasculitis")
    ]

def gastrointestinal(data):
    return [
        html.Br(),
        dbc.Label("Lupus peritonitis"),
        dbc.Label("Abdominal serositis or ascites"),
        dbc.Label("Lupus enteritis/colitis"),
        dbc.Label("Malabsorption"),
        dbc.Label("Protein losing enteropathy"),
        dbc.Label("Intestinal pseudo-obstruction"),
        dbc.Label("Lupus hepatitis"),
        dbc.Label("Acute lupus cholecystitis"),
        dbc.Label("Acute lupus pancreatitis")
    ]

def ophthalmic(data):
    return [
        html.Br(),
        dbc.Label("Orbital inflammation/myositis/proptosis"),
        dbc.Label("Keratitis – severe"),
        dbc.Label("Keratitis – mild"),
        dbc.Label("Anterior uveitis"),
        dbc.Label("Posterior uveitis/retinal vasculitis – severe"),
        dbc.Label("Posterior uveitis/retinal vasculitis – mild"),
        dbc.Label("Episcleritis"),
        dbc.Label("Scleritis – severe"),
        dbc.Label("Scleritis – mild"),
        dbc.Label("Retinal/choroidal vaso-occlusive disease"),
        dbc.Label("Isolated cotton-wool spots (cytoid bodies)"),
        dbc.Label("Optic neuritis"),
        dbc.Label("Anterior ischaemic optic neuropathy")
    ]

def renal(data):
    return [
        html.Br(),
        dbc.Label("Systolic blood pressure (mmHg)"),
        dbc.Label("Diastolic blood pressure (mmHg)"),
        dbc.Label("Accelerated hypertension"),
        dbc.Label("Urine dipstick protein (+ = 1, + + = 2, + + + = 3)"),
        dbc.Label("Urine albumin-creatinine ratio mg/mmol"),
        dbc.Label("Urine protein-creatinine ratio mg/mmol"),
        dbc.Label("24 hours urine protein (g)"),
        dbc.Label("Nephrotic syndrome"),
        dbc.Label("Creatinine (plasma/serum) μmol/l"),
        dbc.Label("GFR (calculated) ml/min/1,73 m2"),
        dbc.Label("Active urinary sediment"),
        dbc.Label("Active nephritis")
    ]

def haematological(data):
    return [
        html.Br(),
        dbc.Label("Haemoglobin (g/dl)"),
        dbc.Label("Total white cell count (×  109/l)"),
        dbc.Label("Neutrophils (×  109/l)"),
        dbc.Label("Lymphocytes (×  109/l)"),
        dbc.Label("Platelets (×  109/l)"),
        dbc.Label("TTP"),
        dbc.Label("Evidence of active haemolysis"),
        dbc.Label("Coombs’ test positive (isolated)")
    ]


def summary_view(data):
    return []


def bilag(data):
    tabs = [dbc.Tabs([
                make_mini_tab(constitutional(data), "Constitutional"),
                make_mini_tab(mucocutaneous(data), "Mucocutaneous"),
                make_mini_tab(neuropsychiatric(data), "Neuropsychiatric"),
                make_mini_tab(muscoloskeletal(data), "Muscoloskeletal"),
                make_mini_tab(cardiorespiratory(data), "Cardiorespiratory"),
                make_mini_tab(gastrointestinal(data), "Gastrointestinal"),
                make_mini_tab(ophthalmic(data), "Ophthalmic"),
                make_mini_tab(renal(data), "Renal"),
                make_mini_tab(haematological(data), "Haematological")
            ]
        )
    ]

    return [html.Div(html.H3("BILAG"), style={"align": "center"}),
            html.Br(),
            html.Button(children="Random Test Data", id="bilag-random-data", n_clicks=0),
            html.Br(),
            html.Br(),
            make_row([
                make_column(3, summary_view(data), "Summary"),
                make_column(4, tabs, "Topics"),
                make_column(5, [], "Fancy View", border_left=True)
            ]),
            html.Br()
    ]



def pdf_upload():
    """
    uppermost layout of select_csv page
    """ 


    children2 = html.Div(id="output-text-upload-pdf-file", children= [html.P("No data")], style={"padding": 15})
    children3 = html.Div(id="output-text-upload-pdf-text-extraction1", style={"padding": 15})
    children4 = html.Div(id="output-text-upload-pdf-text-extraction2", style={"padding": 15})


    tabs = [dbc.Tabs([
                make_mini_tab(children3, "1 column PDF"),
                make_mini_tab(children4, "Text PDF")
            ]
        )
    ]

    children=[
            html.Div(
                className="row",
                children =[
                    html.Div(
                        className="four columns",
                        children=[
                            html.Div(
                                dcc.Markdown(children="#### PDF upload")
                            ),
                            dcc.Store("pdf_parsed", data={}),
                            html.Br(),
                            dcc.Upload(
                                id="upload-pdf-text-extraction-page",
                                accept= ".pdf",
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
                            html.Div(id="output-data-upload-text-extraction", style={"fontsize":10})
                        ]
                    )
                ],
                style={'justifyContent': 'center'}
            ),
            make_row([
                make_column(6, children2, "Original File"),
                make_column(6, tabs, "Text", border_left=True)
            ])
    ]

    return children

def text_extraction():
    """
    uppermost layout of csv_dashboard page
    """ 
    children=[
        dcc.Location(id="url"),
        sidebar,
        html.Div(id="page-content", className="content")
    ]

    return children