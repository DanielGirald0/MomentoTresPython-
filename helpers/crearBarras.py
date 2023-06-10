import matplotlib.pyplot as plt
def graficarEnBarras(dataFrame, campoX, campoY, nombreGrafica):
    colores = ['green', 'red']
    salarioPromedio = dataFrame.groupby(campoX)[campoY].mean()

    # Obtener los valores únicos de ciudad como lista ordenada
    ciudades = sorted(list(set(salarioPromedio.index)))

    # Obtener los valores correspondientes de cantidad de árboles
    arboles = salarioPromedio[ciudades]

    # Generar la gráfica
    plt.bar(ciudades, arboles, color=colores)

    plt.title("Análisis de Siembras de Árboles")
    plt.xlabel("Ciudad")
    plt.ylabel("Árboles")

    plt.savefig(f'./assets/img/{nombreGrafica}.png')

'''def graficarEnBarras(dataFrame,campoX,campoY,nombreGrafica):
    colores=['green','red']
    salarioPromedio=dataFrame.groupby(campoX)[campoY].mean()

    #Generar la grafica
    plt.bar(salarioPromedio.index,salarioPromedio,color=colores)

    plt.title("Analisis De Siembras De Arboles ")
    plt.xlabel("Ciudad")
    plt.ylabel("Arboles")

    plt.savefig(f'./assets/img/{nombreGrafica}.png') '''