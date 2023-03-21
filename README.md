# pi1_08
.Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = as123)

.Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

.De haber fechas, deberán tener el formato AAAA-mm-dd

.Los campos de texto deberán estar en minúsculas, sin excepciones

.El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de   duración: min (minutos) o season (temporadas)
y a la vez me piden que realice una app donde se pueda hacer esto:

._Buscar la película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.

._Saber la cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. 

._Saber la Cantidad de películas por plataforma con filtro de PLATAFORMA.

._Saber el actor que más se repite según plataforma y año.
