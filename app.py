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
print(gdf.head())
print(gdf.geometry)
print(gdf.columns)

# Mapa
m = folium.Map(location=[-34.6, -58.4], zoom_start=12) # crear mapa
folium.GeoJson(gdf).add_to(m) # añadir 
st_data = st_folium(m, width=700, height=500) # renderizar


# Prueba pyobis
print(pyobis.occurrences.centroid(scientificname='Mola mola', size=1).api_url)

