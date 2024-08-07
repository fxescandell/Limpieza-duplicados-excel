# functions.py
import pandas as pd

def load_excel(file_path):
    """Carga un archivo Excel y devuelve un DataFrame de pandas.
    
    Args:
        file_path (str): La ruta del archivo Excel.

    Returns:
        DataFrame: Un DataFrame de pandas con los datos del archivo Excel.
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

def remove_duplicates(df, subset):
    """Elimina duplicados en el DataFrame basado en un subconjunto de columnas.
    
    Args:
        df (DataFrame): El DataFrame de pandas.
        subset (list): Lista de nombres de columnas a considerar para identificar duplicados.

    Returns:
        DataFrame: Un DataFrame sin filas duplicadas basado en el subset proporcionado.
    """
    try:
        df_no_duplicates = df.drop_duplicates(subset=subset)
        return df_no_duplicates
    except Exception as e:
        print(f"Error al eliminar duplicados: {e}")
        return df
