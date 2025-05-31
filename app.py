# Interfaz
import streamlit as st
import folium
from streamlit_folium import st_folium

# Procesar datos
import geopandas as gpd

# API Datos
import pyobis
from pyobis import occurrences

# Datos
gdf = gpd.read_file("MEOW/meow_ecos.shp")

indices = [
    2, # Norte Brasil
    9, # Centro Chile  
    15, # Bahamas
    21, # Bemuda
    33, # Centro Chile

    36, 39, 41, 42, 44, 
    46, 60, 61, 62, 67, 69, 72, 73, 80, 83, 91, 92,
    
    107, 113, 118, 122, 124, 129, 130, 132, 135,
    138, 140, 146, 147, 148, 152, 153, 173, 174,
    175, 177, 178, 182, 190, 191, 194, 196,

    204
]

gdf = gdf.iloc[indices]


# Mapa
m = folium.Map(location=[-34.6, -58.4], zoom_start=0) # crear mapa
folium.GeoJson(
    gdf,
    tooltip=folium.GeoJsonTooltip(fields=['ECOREGION'], aliases=['Ecoregión'])
    ).add_to(m) # añadir 
st_data = st_folium(m, width=700, height=500) # renderizar


# Prueba pyobis
# print(pyobis.occurrences.centroid(scientificname='Mola mola', size=1).api_url)

