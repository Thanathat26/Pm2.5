import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

# Incorporate data
df = pd.read_csv('P_ML2.csv')

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define graph types
graph_types = {"Line Chart": px.line, "Scatter Plot": px.scatter, "Bar Plot": px.bar, "Histogram": px.histogram}

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Predict PM2.5", className="text-center"),
            dbc.Col([
                html.Hr(),
                html.Label("Select type of graph:"),
                dcc.Dropdown(
                    id="graph-type",
                    options=[{"label": option, "value": option} for option in graph_types.keys()],
                    value="Line Chart",
                ),
                html.Button("Update Graph", id="update-button", n_clicks=0),
            ])
        ], width=6),
        dbc.Col([
            dcc.Graph(id="graph")
        ])
    ], className="mt-4"),
    dbc.Row([
        dbc.Col([
            html.H2("Predictions", className="text-center"),
            dash_table.DataTable(
                id="predictions-table", data=df.to_dict("records"), page_size=6
            ),
        ])
    ], className="mt-4")
])


@app.callback(
    [Output("graph", "figure")],
    [Input("update-button", "n_clicks"), Input("graph-type", "value")],
)
def update_graph(n_clicks, graph_type):
    if n_clicks > 0:
        return [graph_types[graph_type](df, x="DATETIMEDATA", y="prediction_label", title="PM2.5 Values")]
    else:
        return [] 

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
