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

fig.update_layout(
    coloraxis_colorbar=dict(
        title="PM2.5 ",
        titleside="right"
    ),
    coloraxis=dict(
        colorscale=[[0, "green"], [0.5, "yellow"], [1, "red"]],
        cmin=gapminder['prediction_label'].min(),
        cmax=gapminder['prediction_label'].max()
    )
)

fig.show()