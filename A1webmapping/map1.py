import folium
import pandas

#Importation of data, commit functions
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map([38.58, -99.09], zoom_start=6)

#Features
fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

#Volcano Layer
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 7, popup=str(el)+" m", fill_color=color_producer(el), color = 'grey', fill_opacity=0.8))

#Population Layer
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=lambda x: {'fillColor':'green' 
                          if x['properties']['POP2005'] < 10000000 
                          else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
                          else 'red'}))

#Layer Control
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")