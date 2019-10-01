import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data['LON'])
name = list(data['NAME'])

map = folium.Map(location=[40.643006, -111.935535], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, n in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=n, icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")