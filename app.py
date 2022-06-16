from sre_parse import State
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import pathlib
import plotly.express as px
import pandas as pd

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("datasets").resolve()

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP,dbc.icons.FONT_AWESOME],
    suppress_callback_exceptions=True
)

## Import other pages
from pages import national,home,regional,about,graficas,tabs_national,tabs_regional,home2
from pages.elements import nat_forest,nat_temperature,reg_forest,reg_temperature

# Style of the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# Content style
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

### CUSTOM COMPONENTS

sidebar = html.Div(
    [
        html.H2("Corest", className="display-4"),
        html.Hr(),
        html.P(
            "lorem ipsum", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("National", href="/prediction", active="exact"),
                dbc.NavLink("Regional", href="/description", active="exact"),
                dbc.NavLink("About", href="/about", active="exact"),
                dbc.NavLink("Graficas", href="/graficas", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

sidebar_responsive=html.Div(className="container-fluid overflow-hidden",
    children=[
        html.Div(className="row vh-100 overflow-auto",
        children=[
            html.Div(className="col-12 col-sm-3 col-xl-2 px-sm-2 px-0 bg-black d-flex sticky-top",
            children=[
                html.Div(className="d-flex flex-sm-column flex-row flex-grow-1 align-items-center align-items-sm-start px-3 pt-4 text-white",
                children=[
                    dbc.NavLink(href="/", className="d-flex align-items-center pb-sm-3 mb-md-0 me-md-auto text-white text-decoration-none",
                    children=[
                        html.Img(src="https://www.collinsdictionary.com/images/full/tree_267376982.jpg", className="w-25 rounded-circle"),
                        html.Span("ECO REST",className="d-none d-md-inline p-2")
                        ]),
                    html.Br(),
                    dbc.Nav(className="nav nav-pills flex-sm-column flex-row flex-nowrap flex-shrink-1 flex-sm-grow-0 flex-grow-1 mb-sm-auto mb-0 justify-content-center align-items-center align-items-sm-start pt-5",id="menu",
                    children=[
                        dbc.NavLink(className="nav-item",href="/",active="exact",
                        children=[
                            html.I(className="fs-5 bi-house"),
                            html.Span("Home",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/prediction",active="exact",
                        children=[
                            html.I(className="fa-solid fa-temperature-low"),
                            html.Span("Predicción",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/description",active="exact",
                        children=[
                            html.I(className="fs-5 bi-table"),
                            html.Span("Departamental",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/about",active="exact",
                        children=[
                            html.I(className="fs-5 bi-people-fill"),
                            html.Span("About",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/graficas",active="exact",
                        children=[
                            html.I(className="fs-5 bi-people-fill"),
                            html.Span("Graficas",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/tabs_national",active="exact",
                        children=[
                            html.I(className="fs-5 bi-people-fill"),
                            html.Span("National (Tabs)",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/tabs_regional",active="exact",
                        children=[
                            html.I(className="fs-5 bi-people-fill"),
                            html.Span("Regional (Tabs)",className="ms-1 d-none d-sm-inline") 
                        ]),
                        
                    ])
            ])
            ]),
            html.Div(id="page-content",className="col d-flex flex-column h-100 nopadding")
        ]
        )
    ]
)


sidebar_responsive2=html.Div(className="container-fluid overflow-hidden",
    children=[
        html.Div(className="row vh-100 overflow-auto",
        children=[
            html.Div(className="col-12 col-sm-3 col-xl-2 px-sm-2 px-0 bg-black d-flex sticky-top",
            children=[
                html.Div(className="d-flex flex-sm-column flex-row flex-grow-1 align-items-center align-items-sm-start px-3 pt-4 text-white",
                children=[
                    dbc.NavLink(href="/", className="d-flex align-items-center pb-sm-3 mb-md-0 me-md-auto text-white text-decoration-none",
                    children=[
                        html.Img(src="https://www.collinsdictionary.com/images/full/tree_267376982.jpg", className="w-25 rounded-circle"),
                        html.Span("ECO REST",className="d-none d-md-inline p-2")
                        ]),
                    html.Br(),
                    dbc.Nav(className="nav nav-pills flex-sm-column flex-row flex-nowrap flex-shrink-1 flex-sm-grow-0 flex-grow-1 mb-sm-auto mb-0 justify-content-center align-items-center align-items-sm-start pt-5",id="menu",
                    children=[
                        dbc.NavLink(className="nav-item",href="/",active="exact",
                        children=[
                            html.I(className="fs-5 bi-house"),
                            html.Span("Home",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/prediction",active="exact",
                        children=[
                            html.I(className="fa-solid fa-temperature-low"),
                            html.Span("Predicción",className="ms-1 d-none d-sm-inline") 
                        ]),
                        dbc.NavLink(className="nav-item",href="/description",active="exact",
                        children=[
                            html.I(className="bi bi-graph-up"),
                            html.Span("Area descriptiva",className="ms-1 d-none d-sm-inline") 
                        ]),
                        
                        
                    ])
            ])
            ]),
            html.Div(id="page-content",className="col d-flex flex-column h-100 nopadding")
        ]
        )
    ]
)



### LAYOUT AND CONTENT

content = html.Div(className="col d-flex flex-column h-100",
children=[html.Main(className="row")]) 

app.layout = html.Div([dcc.Location(id="url"), sidebar_responsive2, content])


### Callbacks

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home2.layout
    elif pathname == "/prediction":
        return national.layout
    elif pathname == "/description":
        return  national.layout

##Enlaces no usados por ahora
    elif pathname == "/about":
        return about.layout
    elif pathname == "/graficas":
        return graficas.layout
    elif pathname == "/tabs_national":
        return tabs_national.layout
    elif pathname == "/tabs_regional":
        return tabs_regional.layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
    dbc.Container(
        [
            
            html.H1("404: Not found", className="display-3 text-danger"),
            html.P(
                f"The pathname {pathname} was not recognised...",
                className="lead",
            ),
            html.Hr(className="my-2"),

            
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)


### CALLBACKS TABS NATIONAL ###

@app.callback(Output('content_national', 'children'),
              Input('tabs_national', 'value'))
def render_content(tab):
    if tab == 'tab_temperature':
        return nat_temperature.layout
    elif tab == 'tab_eforestation':
        return nat_forest.layout

### END CALLBACKS TABS NATIONAL ###

### CALLBACKS TABS REGIONAL ###

@app.callback(Output('content_regional', 'children'),
              Input('tabs_regional', 'value'))
def render_content(tab):
    if tab == 'tab_temperature_reg':
        return reg_temperature.layout
    elif tab == 'tab_eforestation_reg':
        return reg_forest.layout

### END CALLBACKS TABS REGIONAL ###



## CALLBACKS NATIONAL ##

## Callback Slider
@app.callback(
    Output("LandUsePie","figure"),
    Output("LandUseLines","figure"),
    [Input("year_slider","value")],
    [Input("land_use_drop","value")])

def update_output(value,value_drop):
    df_land=pd.read_csv(DATA_PATH.joinpath("landcoverFAO.csv"))
    df_land["Year"]=df_land["Year"].astype(int)
    df=df_land[(df_land["Year"]>=value[0]) & (df_land["Year"]<=value[1])]
    fig = px.pie(df,values="Value", names="Item")
    fig.update_layout(transition_duration=500)
    fig.update_layout(showlegend=False)

    if value_drop is None:
        fig2 = px.line(df,x="Year", y="Value",color="Item")
    else:
        dff=df[df.Item.str.contains('|'.join(value_drop))]
        fig2 = px.line(dff,x="Year", y="Value",color="Item")
    fig2.update_layout(transition_duration=500)
    fig2.update_layout(showlegend=False)
    return fig,fig2

@app.callback(
    Output('parrafo', 'children'),
    [Input('year_slider', 'value')])
def update_output(value):
    string_exit='Estas viendo datos desde {} hasta {}'.format(value[0],value[1])
    return string_exit


@app.callback(
    Output("forestvs","figure"),
    [Input("year_slider","value")],
    [Input("forestvs_drop","value")]
)
def forestvs(year,variable):
    df_data=pd.read_csv(DATA_PATH.joinpath("output_merge.csv"))
    df=df_data[(df_data["year"]>=year[0]) & (df_data["year"]<=year[1])]
    if variable is None:
        fig2 = px.line(df,x="year",y=df.columns[1:])
    else:
        variable.append("year")
        dff=df[variable]
        fig2 = px.line(dff,x="year", y=dff.columns[:-1])
    fig2.update_layout(transition_duration=500)
    fig2.update_layout(showlegend=False)
    return fig2

## END CALLBACKS NATIONAL ##

if __name__ == "__main__":
    app.run_server(debug=True)