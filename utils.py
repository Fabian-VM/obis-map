from typing import List
import geopandas as gpd

# En el archivo regiones.csv, está la tabla de todas las regiones marinas del mundo registradas
# y delimitadas por polígonos
# Estos indices corresponden a sólo los de interés para la aplicación
CHOOSEN_AREAS_INDEXES = [
    2, 9, 15, 33, 36, 39, 41, 42, 44, 46, 60, 
    61, 62, 67, 69, 72, 73, 91, 92,
    107, 113, 118, 122, 124, 130, 132,
    138, 140, 146, 147, 148, 152, 173, 174,
    175, 178, 182, 190, 194, 204
]

# geopandas.GeoDataFrame es igual que un pandas DataFrame
# pero con una columna especial llamada "geometry".
# Esa columna contiene objetos geométricos shapely, en este caso
# la clase shapely.Polygon, para representar un área geográfica.
def get_geodataframe(path: str, indexes: List[int]) -> gpd.GeoDataFrame:
    full_dataframe = gpd.read_file(path)
    return full_dataframe.iloc[indexes]

