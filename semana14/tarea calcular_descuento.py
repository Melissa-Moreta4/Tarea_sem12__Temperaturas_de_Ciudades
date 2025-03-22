#Tarea Sem 14 "Calcular descuento".
"""Esta función se llama calcular_descuento en donde toma dos parámetros:
el monto total de la compra.
un valor predeterminado para el porcentaje de descuento.

La función calcula el descuento, junto con el porcentaje al monto total de la compra.
La función devuelve el monto del descuento calculado."""

def calcular_descuento(monto_total, porcentaje_descuento):
    descuento = monto_total * (porcentaje_descuento/100)
    return descuento

if __name__=="__main__":
    monto_de_compra1 = 2500
    monto_de_compra2 = 4600

    #llamar a la función para calcular el descuento1
    porcentaje_descuento = 10
    descuento1 = calcular_descuento(monto_de_compra1, porcentaje_descuento)
    print(f"Monto total de la compra: {monto_de_compra1}")
    print(f"El descuento es: {descuento1}")

    #llamar a la función para calcular el descuento2
    porcentaje_descuento = 15
    descuento2 = calcular_descuento(monto_de_compra2, porcentaje_descuento)
    print(f"Monto total de la compra: {monto_de_compra2}")
    print(f"El descuento es: {descuento2}")

