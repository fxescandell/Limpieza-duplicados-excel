# Limpieza-duplicados-excel

Limpia un listado de excels de duplicados de usuarios con el mismo mail

# Documentación de functions.py

Este archivo contiene funciones útiles para trabajar con archivos de Excel y limpiar datos duplicados. A continuación, se explica de manera general qué hace cada función, qué columnas utiliza y cómo es el archivo final que se genera.

## ¿Qué hace este archivo?

1. **Carga archivos de Excel**: Convierte los datos de un archivo de Excel en una tabla que se puede manipular fácilmente.
2. **Elimina duplicados**: Limpia la tabla eliminando las filas que contienen datos repetidos en ciertas columnas.

## ¿Qué columnas utiliza?

Las funciones pueden trabajar con cualquier archivo de Excel que tenga datos organizados en columnas. Por ejemplo, si tienes un archivo con columnas como "Nombre", "Edad" y "Ciudad", estas funciones pueden ayudarte a cargar el archivo y eliminar las filas duplicadas basadas en una o más de estas columnas.

## ¿Cómo es el archivo final que se genera?

Después de usar estas funciones, tendrás una tabla (DataFrame) sin filas duplicadas basada en las columnas que hayas elegido. Por ejemplo, si decides eliminar duplicados basados en las columnas "Nombre" y "Ciudad", la tabla final tendrá solo una fila por cada combinación única de "Nombre" y "Ciudad".

### Ejemplo Práctico

Imagina que tienes un archivo de Excel con la siguiente información:

| Nombre | Edad | Ciudad    |
| ------ | ---- | --------- |
| Juan   | 30   | Madrid    |
| María  | 25   | Barcelona |
| Juan   | 30   | Madrid    |
| Ana    | 40   | Sevilla   |

Si cargas este archivo y decides eliminar duplicados basados en la columna "Nombre", el resultado será:

| Nombre | Edad | Ciudad    |
| ------ | ---- | --------- |
| Juan   | 30   | Madrid    |
| María  | 25   | Barcelona |
| Ana    | 40   | Sevilla   |

### Pasos para Usar las Funciones

1. **Cargar el archivo de Excel**:

   - Usa la función `load_excel` para cargar los datos del archivo Excel.
   - Proporciona la ruta del archivo Excel.

   ```python
   df = functions.load_excel('ruta/al/archivo.xlsx')
   ```

2. **Eliminar duplicados**:

   - Usa la función `remove_duplicates` para eliminar filas duplicadas.
   - Proporciona la tabla y las columnas que quieres considerar para identificar duplicados.

   ```python
   df_no_duplicates = functions.remove_duplicates(df, subset=['Nombre'])
   ```

### ¿Qué pasa si hay un error?

Si ocurre un error (por ejemplo, si el archivo no se puede encontrar o no se puede leer), las funciones mostrarán un mensaje de error y devolverán `None` o la tabla original sin cambios.

## ¿Cómo puedo contribuir?

Si tienes alguna sugerencia o encuentras algún problema, por favor abre un issue o envía un pull request en el repositorio de GitHub.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

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
