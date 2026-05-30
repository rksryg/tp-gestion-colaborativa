# Analisis simple de ventas

ventas = {
    "Mouse": 10,
    "Teclado": 5,
    "Monitor": 3,
    "Auriculares": 8
}

total = sum(ventas.values())

producto_mas_vendido = max(ventas, key=ventas.get)

print("Total de ventas:", total)
print("Producto más vendido:", producto_mas_vendido)
