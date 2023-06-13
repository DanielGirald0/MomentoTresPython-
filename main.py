import pandas as pd
from helpers.crearTablasHTML import crearTabla
from helpers.crearBarras import graficarEnBarras

tabla = pd.read_csv("./data/Siembras.csv") 

#---------------------------Definimos las condiciones logicas
filtro1SantaFe = tabla[(tabla["Ciudad"] == "Santa Fe de Antioquia") & (tabla["Arboles"] > 250)].copy()                                      #filtro # 1
# Convertir la columna "Hectareas" a string antes de aplicar strip
filtro1SantaFe['Hectareas'] = filtro1SantaFe['Hectareas'].astype(str).str.strip()
# Reemplazar caracteres no deseados en la columna "Hectareas"
filtro1SantaFe['Hectareas'] = filtro1SantaFe['Hectareas'].str.replace('\t', '').replace('\n', '')

#filtro2Caucasia = tabla[(tabla["Ciudad"] == "Caucasia")]                                                                                #filtro # 2                                                  
filtro2Caucasia = tabla[(tabla["Ciudad"] == "Caucasia") & (tabla["Vereda"].notnull())]

filtro3Belmira = tabla[(tabla["Ciudad"] == "Belmira") & ((tabla["Vereda"] == "Rio Arriba") | (tabla["Vereda"] == "La Salazar"))]        #filtro # 3

#filtro4Bello = tabla[(tabla["Ciudad"] == "Bello") & ((tabla["Vereda"] == "Quitasol"))]  # filtro # 4
filtro4Bello = tabla[(tabla["Ciudad"] == "Bello") & (tabla["Vereda"] == "Quitasol")]
medias = filtro4Bello.describe()
media_arboles = medias.loc['mean', 'Arboles']  # Media de la columna 'Arboles'

filtro5Caramanta = tabla[(tabla["Ciudad"] == "Caramanta") & (tabla["Arboles"] > 100)]                                                   #filtro # 5

filtro6Yarumal = tabla[(tabla["Ciudad"] == "Yarumal") & (tabla["Vereda"] == "Mallarino")]                                               #filtro # 6

print(f'{filtro5Caramanta}')



#---------------------------Generamos la tabla HTML  con el dataframe de filtro
crearTabla(filtro1SantaFe, "tablaFiltrSantaFe")
crearTabla(filtro2Caucasia, "tablaFiltroCaucasia")
crearTabla(filtro3Belmira, "tablaFiltroBelmira")
crearTabla(filtro4Bello, "tablaFiltroBello")
crearTabla(filtro5Caramanta, "tablaFiltroCaramanta")
crearTabla(filtro6Yarumal, "tablaFiltroYarumal")


#Generar grafica
graficarEnBarras(filtro1SantaFe,'Vereda','Arboles','graficaDeFiltroSantaFe')
graficarEnBarras(filtro2Caucasia,'Vereda','Arboles','graficaDeFiltroCaucasia')
graficarEnBarras(filtro3Belmira,'Vereda','Arboles','graficaDeFiltroBelmira')
graficarEnBarras(filtro4Bello,'Vereda','Arboles','graficaDeFiltroBello')
graficarEnBarras(filtro5Caramanta,'Vereda','Arboles','graficaDeFiltroCaramanta')
graficarEnBarras(filtro6Yarumal,'Vereda','Arboles','graficaDeFiltroYarumal')
