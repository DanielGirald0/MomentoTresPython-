import matplotlib.pyplot as plt

def graficarEnBarras(dataFrame, campoX, campoY, nombreGrafica):
    colores = ['green', 'red']
    datos_agrupados = dataFrame.groupby(campoX)[campoY].sum()

    veredas = datos_agrupados.index
    cantidad_arboles = datos_agrupados.values

    print(f'Datos de la gráfica: {nombreGrafica}')
    print('Veredas:', veredas)
    print('Cantidad de árboles:', cantidad_arboles)

    plt.bar(veredas, cantidad_arboles, color=colores)

    plt.title("Cantidad de Árboles por Vereda")
    plt.xlabel(campoX)
    plt.ylabel(campoY)

    plt.xticks(rotation=90)

    plt.savefig(f'./assets/img/{nombreGrafica}.png')