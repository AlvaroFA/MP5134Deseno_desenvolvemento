import numpy as np
import pandas as pd

'''
Ejercicio 1. Media y mediana ante un valor extremo
Calcular la media y la mediana de las duraciones de seis películas. Repetir el cálculo sin la película más larga y comparar cuánto cambia cada medida.
'''


duracion = pd.Series(
    [90, 76, 71, 90, 111, 201],
    index=["Cleo de 5 a 7", "Las margaritas", "El autoestopista",
           "Baila, muchacha, baila", "La ascensión", "Jeanne Dielman"],
)

print(f"mediana de las duraciones: {duracion.median()}")
print(f"media de las duraciones: {duracion.mean()}")

print(f"media de las duraciones sin la ultima: {duracion.drop("Jeanne Dielman").mean()}")
print(f"media de las duraciones sin la ultima: {duracion.drop("Jeanne Dielman").median()}")

'''
Ejercicio 2. Varianza y desviación típica con ddof
Calcular la varianza y la desviación típica de las edades con NumPy y con pandas, cada una con su valor por defecto. Después, conseguir que NumPy dé el mismo resultado que pandas.
'''

edades = np.array([20, 35, 29, 33, 35, 30])
edadesSeries = pd.Series([20, 35, 29, 33, 35, 30])

media =  round(edadesSeries.mean(),3);

varianza = np.var(edades).round(3)
desviacion_tipica = edades.std().round(3)
desviacion_series = round(pd.Series(edades).var(),3)
print(media, varianza, desviacion_tipica, desviacion_series )

print("NumPy, por defecto:  var", round(np.var(edades), 3), "  std", round(np.std(edades), 3))
print("pandas, por defecto: var", round(pd.Series(edades).var(), 3),
      "  std", round(pd.Series(edades).std(), 3))
print("NumPy con ddof=1:    var", round(np.var(edades, ddof=1), 3),
      "  std", round(np.std(edades, ddof=1), 3))


'''
Ejercicio 3. Cuartiles y rango intercuartílico
Calcular el primer cuartil, la mediana y el tercer cuartil, el rango intercuartílico (IQR) y el umbral superior de la regla
. Mostrar los valores que superan ese umbral.
'''
lectura = pd.Series([10, 15, 20, 20, 25, 30, 40, 90])

q1, q2, q3 = np.percentile(lectura, [25, 50, 75])

mediana = lectura.median()
rango = q3-q1
limite_superior = q3+1.5*rango
limite_inferior = q3-1.5*rango
print(q1,q2,q3, mediana, rango, limite_inferior,limite_superior)

superior =lectura[lectura>limite_superior ].to_list
inferior =lectura[lectura<limite_inferior ].to_list
entre = lectura.between(limite_inferior,limite_superior)
print(inferior, superior)
print(entre.sum())
