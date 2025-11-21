"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


import pandas as pd

def pregunta_13():
    ruta_tbl2 = "files/input/tbl2.tsv"
    ruta_tbl0 = "files/input/tbl0.tsv"

    datos_tbl2 = pd.read_csv(ruta_tbl2, sep="\t")
    datos_tbl0 = pd.read_csv(ruta_tbl0, sep="\t")

    combinada = pd.merge(datos_tbl2, datos_tbl0, on="c0")

    suma_por_c1 = combinada.groupby("c1")["c5b"].sum()

    return suma_por_c1

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
