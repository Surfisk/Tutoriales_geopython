#Para abrir imagenes landsat 8


from pystac_client import Client  #Abrir libreria de pystac
from shapely.geometry import Point #libreria para la coordenada 

# Para conectarse al STAc por API
cmr_api_url = "https://cmr.earthdata.nasa.gov/stac/LPCLOUD" #el url con la pagina para acceder a las imagenes 
client = Client.open(cmr_api_url)


# collecion, coordenadas, y fecha 
search = client.search(
    collections=["HLSL30.v2.0"],
    intersects=Point(-73.24, -39.81), #coordenada valdivia
    datetime="2019-02-01/2022-03-30",
) # nasa cmr cloud cover filtering is currently broken: https://github.com/nasa/cmr-stac/issues/239

# cantidad de resultados 
items = search.get_all_items()
print(len(items))

items_sorted = sorted(items, key=lambda x: x.properties["eo:cloud_cover"]) # eligiendo y filtrando por cubierta de nubes 
item = items_sorted[1]
print(item) #para mostrar imagen elegida 

print(item.assets["browse"].href)  #link con la imagen 
