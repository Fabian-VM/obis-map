import datetime
from enum import Enum
from typing import List
import geopandas as gpd
import pandas as pd


# Tipos posibles de conversión
class DATATYPE(Enum):
    INT = int
    FLOAT = float
    STR = str
    BOOL = bool
    DATETIME = datetime

"""
Imprimir los tipos de datos de las columnas de un dataframe
"""
def print_datatypes(df: pd.DataFrame):
    for col in df.columns:
        print(col, df[col].dtype)


def convert_type(value, new_type: DATATYPE, default_value):
    try:
        #print("intentando convertir un ",new_type, " de valor ", value, "...")
        if new_type == DATATYPE.INT:
            return new_type.value(float(value))
        return new_type.value(value)
    except:
        #print("no se pudo convertir ", value, ", usando valor por defecto...")
        return default_value

"""
Limpiar una columna de un dataframe

Entradas:
- df: dataframe de entrada
- col: columna a limpiar y convertir
- new_type: el nuevo tipo de dato a aplicar
- default: valor por defecto para las celdas vacias de la columna
"""
def clean_column(df: pd.DataFrame, col: str, new_type: DATATYPE, default_value) -> pd.DataFrame:
    df[col] = df[col].fillna(default_value)

    if new_type == datetime:
        # Tratamiento especial para conversión a datetime
        df[col] = pd.to_datetime(df[col], errors='coerce')
    else:
        df[col] = df[col].apply(lambda x: convert_type(x, new_type, default_value))

    df[col] = df[col].fillna(default_value)    
    return df

"""
Verificar que un dataframe contiene todas las columnas especificadas, 
y añadirlas si no se encuentran allí

Entradas:
- df: dataframe de entrada
- cols: arreglo de strings con todas las columnas que se esperan encontrar
"""
def check_missing_columns(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    for col in cols:
        if col not in df.columns:
            df[col] = None
    return df


"""
Dado un dataframe de registros de animales, agrupar por una determinada columna
el conteo de los mismos, e incluir la cantidad de registros agrupados por grupo
Entradas:
- df: el dataframe a procesar
- col: la columna cuyos valores serán usados para agrupar las filas


FALTA IMPLEMENTAR: Contar correctamente en base a:
# Aceptar si absence = false  # algunos puntos vacios son registrados por temas estadisticos
# && (organismQuantityType == "individuals" && organismQuantity != 0) || individualCount != 0
"""
def count_by(df: pd.DataFrame, col: str) -> pd.DataFrame:
    groups = df.groupby(col)
    # pandas.DataFrame con los datos procesados y agrupados por la columna especificada
    result = pd.DataFrame(columns=[col, "quantity", "registriesQuantity"])

    for group_name, group_dataframe in groups:
        result = pd.concat([
            result, 
            pd.DataFrame({
                col: [group_name],
                "quantity": [group_dataframe["individualCount"].sum()],
                "registriesQuantity": [len(group_dataframe)]
            })
        ], ignore_index=True)
    return result