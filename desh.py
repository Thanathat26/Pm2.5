import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dash_table, dcc
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Incorporate data
df = pd.read_csv('P_ML2.csv')

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Predict PM2.5", className="text-center"),
            dbc.Col([html.Hr()]),
            dcc.Graph(id='graph', figure=px.line(df, x='DATETIMEDATA', y='prediction_label', title='PM2.5 Values')),
        ])
    ], className="mt-4"),
    dbc.Row([
        dbc.Col([
            html.H2("Predictions", className="text-center"),
            dash_table.DataTable(data=df.to_dict('records'), page_size=6),
        ])
    ], className="mt-4")
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)