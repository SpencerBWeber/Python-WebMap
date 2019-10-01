import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data['LON'])
elev = list(data["ELEV"])
name = list(data['NAME'])

map = folium.Map(location=[40.643006, -111.935535], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html="Name: %s\n Elevation: %s" % ( name, el), width=200, height=60)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")