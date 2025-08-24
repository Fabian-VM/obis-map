from obis_service import *
from utils import *

# Interfaz
import streamlit as st
import folium
from streamlit_folium import st_folium

# Cargar archivo
polygons_dataframe = get_geodataframe("MEOW/meow_ecos.shp", CHOOSEN_AREAS_INDEXES)

# Función de obtención de datos
@st.dialog("ECOREGION INFORMATION")
def show_area_data(feature):
    text_placeholder = st.empty()
    text_placeholder.write("Loading OBIS data...")
    dataframe_placeholder = st.empty()

    eco_code = feature['properties']['ECO_CODE']
    polygon_text = polygons_dataframe.loc[polygons_dataframe['ECO_CODE'] == eco_code, 'geometry'].iloc[0]
    result = get_area_data(polygon_text=polygon_text)

    result.index = range(1, len(result)+1)
    text_placeholder.write(f"Found {len(result)} species:")
    dataframe_placeholder.write(result)

# Folium mapa
folium_map = folium.Map(location=[-20, -60], zoom_start=3)
geojson_drawing = folium.GeoJson(
    polygons_dataframe,
    tooltip=folium.GeoJsonTooltip(fields=['ECOREGION'], aliases=['Ecoregion']),
    highlight_function=lambda x:{'weight':3, 'color':'blue', 'fillOpacity': 0.6}
)
geojson_drawing.add_to(folium_map)
st_data = st_folium(folium_map, width=1000, height=800) # Inyectar mapa folium en streamlit

# Obtener el último poligono al que se le hizo click
if st_data.get('last_active_drawing'):
    feature = st_data['last_active_drawing']
    show_area_data(feature)
