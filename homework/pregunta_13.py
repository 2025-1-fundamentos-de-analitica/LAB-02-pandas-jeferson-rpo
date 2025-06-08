"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
import os

def pregunta_13():
    base_path = os.path.dirname(__file__)
    parent_path = os.path.dirname(base_path)

    # Rutas de archivos
    file0 = os.path.join(parent_path, "files", "input", "tbl0.tsv")
    file2 = os.path.join(parent_path, "files", "input", "tbl2.tsv")

    # Lectura de archivos
    tbl0 = pd.read_csv(file0, sep="\t")
    tbl2 = pd.read_csv(file2, sep="\t")

    # Hacemos merge por la clave c0
    combinada = pd.merge(tbl0, tbl2, on="c0")

    # Agrupamos por c1 y sumamos los valores de c5b
    resultado = combinada.groupby("c1")["c5b"].sum().sort_index()

    return resultado

"""
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
"""
