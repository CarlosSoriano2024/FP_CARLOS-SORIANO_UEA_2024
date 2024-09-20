def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

monto_compra_1 = 200  # Ejemplo de monto total de la compra
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

monto_compra_2 = 300  # Ejemplo de otro monto total de la compra
porcentaje_descuento_2 = 15  # Ejemplo de porcentaje de descuento
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

print("Llamada 1:")
print("Monto del descuento:", descuento_1)
print("Monto final a pagar después del descuento:", monto_final_1)
print("\nLlamada 2:")
print("Monto del descuento:", descuento_2)
print("Monto final a pagar después del descuento:", monto_final_2)