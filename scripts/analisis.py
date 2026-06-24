# Analisis de ventas

ventas = {
    "Mouse": 17,
    "Teclado": 9,
    "Monitor": 3,
    "Auriculares": 8
}

ventas_totales = 0

for cantidad in ventas.values():
    ventas_totales += cantidad

producto_mas_vendido = max(ventas, key=ventas.get)

print("Ventas totales:", ventas_totales)
print("Producto mas vendido:", producto_mas_vendido)

archivo = open("resultados/resumen.txt", "w")

archivo.write("ANALISIS DE VENTAS\n")
archivo.write("Ventas totales: " + str(ventas_totales) + "\n")
archivo.write("Producto mas vendido: " + producto_mas_vendido)

archivo.close()

print("Resumen guardado en resultados/resumen.txt")
