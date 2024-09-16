def calcular_promedio_temperaturas(datos_temperaturas):
  """
  Calcula la temperatura promedio de cada ciudad en un conjunto de datos.

  Args:
    datos_temperaturas: Un diccionario donde las claves son los nombres de las ciudades
      y los valores son listas de listas, donde cada lista interna representa una semana
      y contiene las temperaturas diarias.

  Returns:
    Un diccionario donde las claves son los nombres de las ciudades y los valores son
      las temperaturas promedio.
  """

  promedios = {}
  for ciudad, semanas in datos_temperaturas.items():
    todas_temperaturas = [temperatura for semana in semanas for temperatura in semana]
    promedio_ciudad = sum(todas_temperaturas) / len(todas_temperaturas)
    promedios[ciudad] = promedio_ciudad
  return promedios

# Ejemplo de uso:
datos = {
    "Ciudad A": [[20, 22, 21, 23], [25, 24, 26, 25], [18, 19, 20, 21], [22, 23, 24, 25]],
    "Ciudad B": [[15, 17, 16, 18], [20, 19, 21, 20], [12, 13, 14, 15], [18, 19, 20, 19]],
    "Ciudad C": [[28, 30, 29, 31], [32, 31, 33, 32], [25, 26, 27, 28], [30, 31, 32, 31]]
}

resultado = calcular_promedio_temperaturas(datos)
print(resultado)