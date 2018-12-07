import folium
import pandas
from geopy.geocoders import ArcGIS

def find_my_color(elev):
	if elev<=1500:
		return "blue"
	elif 1500<elev<2300:
		return "green"
	else:
		return "red"
nom=ArcGIS()
r=nom.geocode("39 Elm Street,Toronto,Canada")

map=folium.Map(location=[r.latitude,r.longitude],zoom_start=6,tiles="openstreetmap")
fg=folium.FeatureGroup(name="My map")
#fg.add_child(folium.Marker(location=[r.latitude,r.longitude],popup="Downtown Toronto",icon=folium.Icon(color="blue")))
fg.add_child(folium.Circle(location=[r.latitude,r.longitude],radius=10,popup="New popup"))
#fg.add_child(folium.CircleMarker(location=[r.latitude,r.longitude],radius=10,popup="again New popup"))

map.add_child(fg)
map.save("new_map.html")


#multiple points
for cor in [[r.latitude,r.longitude],[r.latitude+1,r.longitude+1],[r.latitude+1,r.longitude+1]]:
    fg.add_child(folium.Marker(location=cor,popup="Downtown Toronto",icon=folium.Icon(color="blue")))
    
map.add_child(fg)
map.save("new_map1.html")


#adding multiple cordinates and popup msg from a comma seprated txt file
r_file=pandas.read_csv("Volcanoes.txt")

#fetch latitude,longitue and elevation from the table in list
lat=list(r_file.LAT)
lon=list(r_file.LON)
elev=list(r_file.ELEV)

for la,lo,el in zip(lat,lon,elev):
	fg.add_child(folium.Marker(location=[la,lo],popup=str(el)+"meter",icon=folium.Icon(color="blue")))
	
map.add_child(fg)
map.save("new_map2.html")

for la,lo,el in zip(lat,lon,elev):
	fg.add_child(folium.Marker(location=[la,lo],popup=str(el)+"meter",icon=folium.Icon(color=find_my_color(el))))
	
map.add_child(fg)
map.save("new_map3.html")




