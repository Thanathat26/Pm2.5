import plotly.express as px
import pandas as pd
import geopandas as gpd
gapminder = pd.read_csv('P_MLMap.csv')
print(gapminder.head(15))
fig = px.choropleth(gapminder,
                    locations="iso_alpha",
                    color="prediction_label",
                    scope="asia", 
                    animation_frame="DATETIMEDATA",
                   )

fig.show()