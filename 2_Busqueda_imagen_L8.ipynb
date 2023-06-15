{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0aa70497-e160-417e-b016-8dc0e6ca2d7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "268\n",
      "<Item id=HLS.L30.T18GXA.2019039T143525.v2.0>\n",
      "https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-public/HLSL30.020/HLS.L30.T18GXA.2019039T143525.v2.0/HLS.L30.T18GXA.2019039T143525.v2.0.jpg\n"
     ]
    }
   ],
   "source": [
    "#Para abrir imagenes landsat 8\n",
    "\n",
    "\n",
    "from pystac_client import Client  #Abrir libreria de pystac\n",
    "from shapely.geometry import Point #libreria para la coordenada \n",
    "\n",
    "# Para conectarse al STAc por API\n",
    "cmr_api_url = \"https://cmr.earthdata.nasa.gov/stac/LPCLOUD\" #el url con la pagina para acceder a las imagenes \n",
    "client = Client.open(cmr_api_url)\n",
    "\n",
    "\n",
    "# collecion, coordenadas, y fecha \n",
    "search = client.search(\n",
    "    collections=[\"HLSL30.v2.0\"],\n",
    "    intersects=Point(-73.24, -39.81), #coordenada valdivia\n",
    "    datetime=\"2019-02-01/2022-03-30\",\n",
    ") # nasa cmr cloud cover filtering is currently broken: https://github.com/nasa/cmr-stac/issues/239\n",
    "\n",
    "# cantidad de resultados \n",
    "items = search.get_all_items()\n",
    "print(len(items))\n",
    "\n",
    "items_sorted = sorted(items, key=lambda x: x.properties[\"eo:cloud_cover\"]) # eligiendo y filtrando por cubierta de nubes \n",
    "item = items_sorted[1]\n",
    "print(item) #para mostrar imagen elegida \n",
    "\n",
    "print(item.assets[\"browse\"].href)  #link con la imagen \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25fca2af-fda4-4350-8e11-56c469697362",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
