from dash import html , dcc
import plotly.graph_objects as go

import json

#The information was taken from:  https://github.com/kaefee/dash-template-repo

class mapcol_departamentos:
    """A Class to represent a map of Colombia with two Layers, one for Municipios and 
    the second one for markers as overlay
    
    based in json file of 
    https://www.kaggle.com/code/alfredomaussa/colombia-municipios/notebook?scriptVersionId=39794627
    
    Towns codes available in
    https://www.dane.gov.co/files/censo2005/provincias/subregiones.pdf

    """
    def __init__(self,map_title:str, ID:str,df):
        """__init__ _summary_

        Args:
            map_title (str): Titulo del mapa, html H4 element
            ID (str): css id to use with callbacks
            df (_type_): dataframe with info to use in choropleth
            markers (_type_): small point as overlay in map
        """        
        self.map_title = map_title 
        self.id = ID
        self.df = df 

 
    @staticmethod
    def figura(self):
        with open('datasets/jsonmaps/colombia.geo.json', encoding='utf-8') as json_file:
            departamentos = json.load(json_file)
        for i, each in enumerate(departamentos["features"]):
            departamentos["features"][i]['id']=departamentos["features"][i]['properties']['DPTO']

        mapa = go.Choroplethmapbox(
            geojson=departamentos, 
            locations=self.df.COD_DPTO, 
            z=self.df['COUNT'],
            colorscale="dense",
            text=self.df.DEPARTAMENTO,
            marker_opacity=0.9, 
            marker_line_width=0.5,
            colorbar_title = "COP",
            )
        annotations = [
            dict(
                showarrow=False,
                align="right",
                text="",
                font=dict(color="#000000"),
                bgcolor="#f9f9f9",
                x=0.95,
                y=0.95,
            )
        ]

        fig = go.Figure(data=mapa)

        

        fig.update_layout(
            geo_scope='south america',
            mapbox_style="carto-darkmatter",
            mapbox_zoom=4, 
            mapbox_center = {"lat": 6.88970868, "lon": -74.2973328},
            annotations=annotations,
            height=400,
            font=dict(
                color="white"
            )),

        
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
        })
        
        return fig


    def display(self):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=mapcol_departamentos.figura(self), id=self.id)
                ])
                
            ]
        )
        return layout
    

    #plot according to latitude and longitude

    @staticmethod
    def figura2(self, latitude, longitude):
        with open('datasets/jsonmaps/colombia.geo.json', encoding='utf-8') as json_file:
            departamentos = json.load(json_file)
        for i, each in enumerate(departamentos["features"]):
            departamentos["features"][i]['id']=departamentos["features"][i]['properties']['DPTO']

        mapa = go.Choroplethmapbox(
            geojson=departamentos, 
            locations=self.df.COD_DPTO, 
            z=self.df['COUNT'],
            colorscale="dense",
            text=self.df.DEPARTAMENTO,
            marker_opacity=0.9, 
            marker_line_width=0.5,
            colorbar_title = "COP",
            )
        annotations = [
            dict(
                showarrow=False,
                align="right",
                text="",
                font=dict(color="#000000"),
                bgcolor="#f9f9f9",
                x=0.95,
                y=0.95,
            )
        ]

        fig = go.Figure(data=mapa)

        

        fig.update_layout(
            geo_scope='south america',
            mapbox_style="carto-darkmatter",
            mapbox_zoom=6, 
            mapbox_center = {"lat": latitude, "lon": longitude},
            annotations=annotations,
            height=400,
            plot_bgcolor= "#040d10",
            paper_bgcolor= "#040d10",
            font=dict(
                color="white"
            )),

        
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_layout({
          "plot_bgcolor": "#040d10",
          "paper_bgcolor": "#040d10",
        })
        
        return fig

    def display2(self, latitude, longitude):   
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=mapcol_departamentos.figura2(self,latitude, longitude), id=self.id)
                ])
                
            ]
        )
        return layout
        
    