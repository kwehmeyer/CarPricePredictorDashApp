# %% Libraries
from logging import PlaceHolder
import dash 
import dash_core_components as dcc
from dash_core_components.Dropdown import Dropdown
from dash_core_components.Markdown import Markdown 
import dash_html_components as html 
from dash.dependencies import Input, Output
import dash_table
import plotly.express as px 
import pandas as pd
import sys 
import os
from random_forest import import_datasets
from random_forest import DataSet, PredData
from random_forest import initialize_models, train_models, show_scores
from datetime import datetime as dt
import markdown
models = {}
# %% External stylesheets 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# %% Funcs

data, predict_x = import_datasets()

# %%
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# %%
app.layout = html.Div(
    children=[
    dcc.Markdown(markdown.introduction),

    dcc.Tabs(id='car-tabs', value='tab-1', 
    children=[

        # Predictions
        dcc.Tab(label='Predictor', value = 'pred-tab',
        children=[
            html.Div([
                dcc.Dropdown(id = 'predict-brand-selector', placeholder = "Select Brand",
                    options=[{'label':x[:-4].capitalize(), 'value': x[:-4]} for x in os.listdir('data')], value = 'Audi'
                ),

                dcc.Dropdown(id = 'predict-model-selector', placeholder = 'Select Model',
                ),
                

                dcc.Dropdown(id = 'predict-transmission-selector', placeholder = "Select Transmission"
                ),

                dcc.Dropdown(id = 'predict-fueltype-selector', placeholder = "Select Fuel Type"
                
                ),

                dcc.Dropdown(id = 'predict-enginesize-selector', placeholder = 'Select Engine Size (L)'),

                dcc.Input(id = 'predict-year-selector', type = 'number', placeholder = 'Year',
                min=1950, max = 2025, step = 1,
                ),

                dcc.Input(id = 'predict-mpg-selector', type = 'number', 
                placeholder = 'MPG', min = 1, max = 150),

                dcc.Input(id = 'predict-mileage-selector', type = 'number',
                placeholder = 'ODO Miles', min = 0),

                html.Div(id = 'predict-selected-car-preview')
                
            ])
        ]
        
        ),


        # Visualizations
        dcc.Tab(label="Visualizations", value='viz-tab', 
        children=[dcc.Markdown(markdown.visualizations_text),

        html.Div(
            [
                html.Div(
                    [

                    dcc.Dropdown( id = 'viz-brand-selector', 
                        options=[{'label':x[:-4].capitalize(), 'value': x[:-4]} for x in os.listdir('data')], value = 'audi',
                        style={'width': '48%', 'display': 'inline-block'}
                    
                ),
                    ]
                ),
                html.Div(
                    [
                    
                    dcc.Dropdown(
                        id = 'viz-component-selector',
                        value = 'mileage',
                        style={'width': '48%', 'display': 'inline-block'}
                    )]
                )
            ], className = "row"
        ),

        html.H2("Sample of Data"),


        html.Div(id='summary-stats'),

        dcc.Graph(id='price-mileage-scatter' ),

        dcc.Graph(id='box-plots' )
        
        ]),

        # About
        dcc.Tab(label="About", value="about-tab",
        children=[
            dcc.Markdown(markdown.about_me_text)
        ])

    ])



])

from callbacks.pred_page_callbacks import *
from callbacks.viz_page_callbacks import *



# %%
if __name__ == '__main__':
    app.run_server(debug=True)
