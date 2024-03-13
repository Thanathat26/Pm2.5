import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dash_table, dcc, Input, Output
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import geopandas as gpd
from plotly.subplots import make_subplots

# Incorporate data
df = pd.read_csv('P_ML2.csv')
df2 = pd.read_csv('t_ML2.csv')
fig = go.Figure(data=[go.Surface(z=df.values)])

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
gapminder = pd.read_csv('P_MLMap.csv')
gapmindertemp = pd.read_csv('T_MLMap.csv')
# Define graph types
graph_types = {
    "Line Chart": px.line,
    "Scatter Plot": px.scatter,
    "Bar Chart": px.bar,
    "Violin Plot": px.violin,
}

# App layout
app.layout = dbc.Container([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("อ้างอิง", href="http://air4thai.pcd.go.th/webV3/#/Home")),
            
        ],
        brand="Predict PM2.5",
        color="primary",
        dark=True,
    ),
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
            html.H2("PM2.5 Map", className="text-center"),
            dcc.Graph(figure=px.choropleth(gapminder,
                    locations="iso_alpha",
                    color="prediction_label",
                    scope="asia", 
                    animation_frame="DATETIMEDATA",
                   ))
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Predictions_PM25", className="text-center"),
            dash_table.DataTable(
                id="predictions-table", data=df.to_dict("records"), page_size=6
            ),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H2("Predictions_TEMP", className="text-center"),
            dash_table.DataTable(
                id="predictions-table", data=df2.to_dict("records"), page_size=6),
                dcc.Graph(figure=px.line(df2, x="DATETIMEDATA", y="prediction_label")),
    dbc.Row([
        dbc.Col([
            html.H2("Temperature Map", className="text-center"),
            dcc.Graph(figure=px.choropleth(gapmindertemp,
                    locations="iso_alpha",
                    color="prediction_label",
                    scope="asia", 
                    animation_frame="DATETIMEDATA",
                   ))
        ])
    ])
        ])
    ])
])


@app.callback(
    Output("graph", "figure"),
    [Input("update-button", "n_clicks"), Input("graph-type", "value")],
)
def update_graph(n_clicks, graph_type):
    if n_clicks > 0:
        try:
            figure = graph_types.get(graph_type, px.line)(df, x="DATETIMEDATA", y="prediction_label", title="ค่า PM2.5")
        except Exception as e:
            figure = px.line(x=["Placeholder"], y=[0])
            print(f"Error: {e}")
        return figure
    else:
        return px.line(x=[""], y=[], title="")

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
