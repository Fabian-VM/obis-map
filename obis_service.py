from calc_service import *

import geopandas as gpd
import pandas as pd
from pyobis import occurrences

def get_area_data(polygon_text: str) -> pd.DataFrame:
    pandas_dataframe = occurrences.search(
        fields="scientificName,absence,organismQuantityType,organismQuantity,individualCount", 
        #size=3,
        geometry=polygon_text
        ).execute()

    # Limpiar dataframe
    pandas_dataframe = check_missing_columns(pandas_dataframe, ["scientificName","absence","organismQuantityType","organismQuantity","individualCount"])
    pandas_dataframe = clean_column(pandas_dataframe, "scientificName", DATATYPE.STR, "")
    pandas_dataframe = clean_column(pandas_dataframe, "absence", DATATYPE.BOOL, False)
    pandas_dataframe = clean_column(pandas_dataframe, "organismQuantityType", DATATYPE.STR, "")
    pandas_dataframe = clean_column(pandas_dataframe, "organismQuantity", DATATYPE.FLOAT, 0.0)
    pandas_dataframe = clean_column(pandas_dataframe, "individualCount", DATATYPE.INT, 0)

    return count_by(pandas_dataframe, "scientificName")
