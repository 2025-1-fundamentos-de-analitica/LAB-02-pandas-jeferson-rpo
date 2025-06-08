"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
import os

def pregunta_06():
    base_path = os.path.dirname(__file__)
    parent_path = os.path.dirname(base_path)
    file_path = os.path.join(parent_path, "files", "input", "tbl1.tsv")
    tbl1 = pd.read_csv(file_path, sep="\t")

    # Extraer valores únicos, convertir a mayúsculas y ordenar
    unique_vals = tbl1['c4'].str.upper().unique()
    return sorted(unique_vals)

# Para probar localmente (no dejar esto si se testea automáticamente)
print(pregunta_06())
"""
    Retorne una lista con los valores unicos de la columna c4 del archivo
    tbl1.csv en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

"""

