import plotly.express as px
import pandas as pd
import geopandas as gpd
gapminder = pd.read_csv('P_MLMap.csv')
print(gapminder.head(15))
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gapminder_map = gapminder.merge(world, left_on='iso_alpha', right_on='iso_a3', how='left')
fig = px.choropleth(gapminder_map,
                    locations="iso_alpha",
                    color="prediction_label",
                    scope="world", 
                    animation_frame="DATETIMEDATA",
                   )
fig.show()