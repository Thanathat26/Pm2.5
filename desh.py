# Import packages
from dash import Dash, html, dash_table, dcc,callback,Output,Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('P_ML.csv')
radio_options = [
    {'label': 'Ozone (O3)', 'value': 'O3'},
    {'label': 'Wind Speed (WS)', 'value': 'WS'},
    {'label': 'Predicted PM2.5', 'value': 'prediction_label'}
]
# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='PM2.5 Prediction Dashboard'), 
    html.Hr(),
    dcc.RadioItems(
        id='controls-and-radio-item',
        options=radio_options,
        value='prediction_label',
        labelStyle={'display': 'inline-block'}  
    ),
    dash_table.DataTable(
        data=df.to_dict('records'),
        page_size=10
    ),
    dcc.Graph(id='selected-column-graph') 
])
@callback(
    Output(component_id='selected-column-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(selected_column):
    if selected_column in ['O3', 'WS','prediction_label']:
        fig = px.histogram(df, x='DATETIMEDATA', y=selected_column, histfunc='avg', color='')
    else: 
        fig = px.histogram(df, x='DATETIMEDATA', y=selected_column)

    return fig
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
