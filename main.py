#Importar librerías
''' importamos las librerias '''
from fastapi import FastAPI
import pandas as pd

# Cargar datos
df_plataformas = pd.read_csv("datos_plataformas.csv")
df_score_count = pd.read_csv("df_score_count_database.csv")

# Crear instancia de FastAPI
app = FastAPI()

# Crear función que llama a get_max_duration
@app.get("/get_max_duration")
async def get_max_duration(anio: int, plataforma: str, tipo_de_duracion: str):
    """ esta funcion encuentra la pelicula con mayor duracion en una determinada plataforma """
    if (anio in df_plataformas["release_year"].values) and \
    (plataforma in df_plataformas["plataforma"].values) and \
    (tipo_de_duracion in df_plataformas["duration_type"].values):
        if tipo_de_duracion == "min":
            resultado = df_plataformas[(df_plataformas["plataforma"] == plataforma) & \
                                       (df_plataformas["release_year"] == anio) & \
                                       (df_plataformas["duration_type"] == tipo_de_duracion)]["duration_int"].max()
            if not pd.isna(resultado):
                nombre = df_plataformas[(df_plataformas["plataforma"] == plataforma) & (df_plataformas["release_year"] == anio) & (df_plataformas["duration_int"] == resultado)]["title"].iloc[0]
                tipo = "movie"
            else:
                nombre = "unknown"
                tipo = "movie"
        elif tipo_de_duracion == "season":
            resultado = df_plataformas[(df_plataformas["plataforma"] == plataforma) & (df_plataformas["release_year"] == anio) & (df_plataformas["duration_type"] == tipo_de_duracion)]["duration_int"].max()
            if not pd.isna(resultado):
                nombre = df_plataformas[(df_plataformas["plataforma"] == plataforma) & (df_plataformas["release_year"] == anio) & (df_plataformas["duration_int"] == resultado)]["title"].iloc[0]
                tipo = "tv show"
            else:
                nombre = "unknown"
                tipo = "tv show"
        else:
            resultado = "no se encontró resultado"
        tupla = [anio, plataforma, tipo_de_duracion, resultado, nombre]
        return f"En el año {tupla[0]}, la plataforma {tupla[1]} tiene una {tipo} de nombre {tupla[4]} en {tupla[3]} {tupla[2]}"
    else:
        return "No se encontró resultado"

# Crear función que llama a get_score_count
@app.get("/score_count")
async def score_count(scored: float, year: int):
    """ esta funcion muestra la cantidad de peliculas con puntaje mayor a xx de determinado año """
    if (year in df_score_count["release_year"].values):
        numero_peli =  df_score_count[(df_score_count["rating_y"] > scored) & (df_score_count["release_year"] == year)].groupby(["plataforma", "release_year", "title"])["rating_y"].mean().groupby(["plataforma", "release_year"]).count()
    else:
        numero_peli = "no hay peliculas con puntaje mayor"
    tupla = [numero_peli]
    return {"Numero de peliculas": tupla[0]}

@app.get("/count_platform")
async def count_platform(plataforma:str):
    if (plataforma in df_score_count["plataforma"].values):
        cantidad_por_plat = df_score_count.groupby("plataforma")["title"].nunique()
    else:
        cantidad_por_plat = "no existe esta plataforma"
    tupla = [cantidad_por_plat, plataforma]
    return f"son {tupla[0]} las peliculas y series en {tupla[1]}"