import pandas as pd
from helpers.crearTablasHTML import crearTabla

tabla = pd.read_csv("./data/Siembras.csv") 

#---------------------------Definimos las condiciones logicas
filtro1SantaFe = tabla[(tabla["Ciudad"].str.contains == "Santa Fe de Antioquia",  case=False) & (tabla["Arboles"] > 250)]                                         #filtro # 1

filtro2Caucasia = tabla[(tabla["Ciudad"] == "Caucasia")]                                                                                #filtro # 2                                                  

filtro3Belmira = tabla[(tabla["Ciudad"] == "Belmira") & ((tabla["Vereda"] == "Rio Arriba") | (tabla["Vereda"] == "La Salazar"))]        #filtro # 3

filtro4Bello = tabla[(tabla["Ciudad"] == "Bello") & ((tabla["Vereda"] == "Quitasol"))]                                                #filtro # 4
medias = filtro4Bello.describe()

filtro5Caramanta = tabla[(tabla["Ciudad"] == "Caramanta") & (tabla["Arboles"] > 100)]                                                   #filtro # 5

filtro6Yarumal = tabla[(tabla["Ciudad"] == "Yarumal") & (tabla["Vereda"] == "Mallarino")]                                               #filtro # 6



print(f'{filtro1SantaFe}')
#print(f'{filtro2Caucasia.describe()}')
#print(filtro3Belmira)



#---------------------------Generamos la tabla HTML  con el dataframe de filtro
#crearTabla(filtro1SantaFe, "tablaFiltroUnoSantaFe")
