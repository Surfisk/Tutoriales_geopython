#Abrir imagenes con API (Application Programming Interface) 


api_url = "https://earth-search.aws.element84.com/v0"

from pystac_client import Client  #Abrir libreria de pystac
client = Client.open(api_url)

collection = "sentinel-s2-l2a-cogs"  # Sentinel-2, Level 2A, COGs    Abrir la información de sentinel COG son un formato util que se pueden acceder facilmente con HTTP 

from shapely.geometry import Point      #pedimos un punto especifico siguiendo una geometria 
point = Point(4.89, 52.37)  # AMS coordinates

search = client.search(                          #para que sean elegidas solo 10 maximos
    collections=[collection],
    intersects=point,
    max_items=10,
)

print(search.matched())  #cuanta informacion coincide 

items = search.get_all_items()  #para datos fueron elegidos 
print(len(items))


for item in items: #para ver los datos
    print(item)
      

assets = items[0].assets  # first item's asset dictionary
print(assets.keys())

item = items[0]        #para ver que info tiene el primer dato, el dato 0 
print(item.datetime)
print(item.geometry)
print(item.properties)

assets = items[0].assets  # para elegir la primera imagen 
print(assets.keys()) 

for key, asset in assets.items():      #para ver la metadata de la primera imagen 
    print(f"{key}: {asset.title}")
     
print(assets["thumbnail"].href)  #imagen referencial

import rioxarray                       #para importar una imagen 
b01_href = assets["B01"].href
b01 = rioxarray.open_rasterio(b01_href)
print(b01)

# para guardar una imagen 
b01.rio.to_raster("B01.tif")