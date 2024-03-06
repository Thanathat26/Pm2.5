# Import packages
from dash import Dash, html, dash_table, dcc,callback,Output,Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('P_ML.csv')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Predict of PM2.5'),
    html.Hr(),
    #dcc.RadioItems(options=['O3', 'WS', 'prediction_label'], value='prediction_label', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),    
    #dcc.Graph(figure=px.line(df, x='DATETIMEDATA', y='O3')),
    #dcc.Graph(figure=px.line(df, x='DATETIMEDATA', y='WS')),
    dcc.Graph(figure=px.scatter(df, x='DATETIMEDATA', y='prediction_label', color='O3'))])

def update_graph(col_chosen):
    fig = px.histogram(df, x='DATETIMEDATA', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
