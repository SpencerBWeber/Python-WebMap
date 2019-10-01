import folium
map = folium.Map(location=[40.643006, -111.935535], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coodinates in [[40.3, -111.5], [49.3, -117.5]]:
    fg.add_child(folium.Marker(location=coodinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")