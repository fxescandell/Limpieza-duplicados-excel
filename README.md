# Limpieza-duplicados-excel

Limpia un listado de excels de duplicados de usuarios con el mismo mail

Aquí tienes un ejemplo de un archivo `README.md` para documentar tu código en GitHub:

````markdown
# functions.py

Este módulo contiene funciones para cargar archivos Excel en un DataFrame de pandas y para eliminar duplicados en el DataFrame basado en un subconjunto de columnas.

## Requisitos

- pandas

Puedes instalar las dependencias necesarias usando pip:

```bash
pip install pandas
```
````

## Funciones

### load_excel

Carga un archivo Excel y devuelve un DataFrame de pandas.

**Parámetros:**

- `file_path` (str): La ruta del archivo Excel.

**Devuelve:**

- `DataFrame`: Un DataFrame de pandas con los datos del archivo Excel. Si ocurre un error, devuelve `None`.

**Ejemplo de uso:**

```python
import functions

df = functions.load_excel('ruta/al/archivo.xlsx')
if df is not None:
    print(df.head())
```

### remove_duplicates

Elimina duplicados en el DataFrame basado en un subconjunto de columnas.

**Parámetros:**

- `df` (DataFrame): El DataFrame de pandas.
- `subset` (list): Lista de nombres de columnas a considerar para identificar duplicados.

**Devuelve:**

- `DataFrame`: Un DataFrame sin filas duplicadas basado en el subset proporcionado. Si ocurre un error, devuelve el DataFrame original.

**Ejemplo de uso:**

```python
import functions

df = functions.load_excel('ruta/al/archivo.xlsx')
if df is not None:
    df_no_duplicates = functions.remove_duplicates(df, subset=['columna1', 'columna2'])
    print(df_no_duplicates.head())
```

## Errores

Ambas funciones manejarán errores internamente y, en caso de ocurrir un error, se imprimirá un mensaje en la consola indicando el tipo de error.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes alguna sugerencia o encuentras algún problema, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

```

Puedes ajustar el contenido según tus necesidades específicas y añadir cualquier otra información relevante que consideres necesaria para los usuarios de tu código.
```
