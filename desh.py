# Import packages
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('P_ML.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.line(df, x='DATETIMEDATA', y='O3')),
    dcc.Graph(figure=px.line(df, x='DATETIMEDATA', y='WS')),
    dcc.Graph(figure=px.scatter(df, x='DATETIMEDATA', y='prediction_label', color='O3'))])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
