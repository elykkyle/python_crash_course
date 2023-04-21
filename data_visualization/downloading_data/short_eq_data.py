import json
import plotly.express as px
from pathlib import Path

path = Path("eq_data/eq_data_30_day_m1.geojson")
all_eq_dicts = json.loads(path.read_text())["features"]
mags, lons, lats, eq_titles = zip(
    *[
        (
            eq_dict["properties"]["mag"],
            eq_dict["geometry"]["coordinates"][0],
            eq_dict["geometry"]["coordinates"][1],
            eq_dict["properties"]["title"],
        )
        for eq_dict in all_eq_dicts
    ]
)

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    title="Global Earthquakes",
    color=mags,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
