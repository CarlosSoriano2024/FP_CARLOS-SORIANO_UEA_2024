# 1. Crear un diccionario
informacion_personal ={
    "nombre": "Andres",
    "edad": 34,
    "ciudad": "El Coca",
    "profesion": "Ingeniero"
}

# 2. Acceder y modificar valores
informacion_personal["ciudad"] = "Sacha"  # Modificar valor de la clave "ciudad"
informacion_personal["profesion"] = "Programador"  # Agregar nueva clave "profesion"

# 3. Verificar existencia de claves y agregar si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "1234567890"  # Agregar clave "telefono" con un número ficticio

# 4. Eliminar una clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar clave "edad"

# 5. Imprimir el diccionario final
print("Diccionario final:")
print(informacion_personal)