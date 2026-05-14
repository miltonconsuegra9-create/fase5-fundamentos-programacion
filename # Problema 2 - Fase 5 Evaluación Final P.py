# Fase 5 - Problema 2

menu = [
    ["Hamburguesa", "Comida Rapida", 18000],
    ["Pizza", "Comida Rapida", 25000],
    ["Ensalada", "Saludable", 14000],
    ["Pasta", "Italiana", 22000],
    ["Sushi", "Japonesa", 30000],
    ["Tacos", "Mexicana", 17000]
]

# Funcion para calcular precio final
def calcular_precio_final(categoria_producto, precio_base,
                          categoria_objetivo, umbral):
    if categoria_producto.lower() == categoria_objetivo.lower() and precio_base > umbral:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base
    return precio_final

print("----- MENU DE PROMOCIONES -----")

# Datos ingresados por usuario
categoria_objetivo = input("Ingrese la categoria objetivo: ")
umbral = float(input("Ingrese el precio minimo para aplicar descuento: "))

print("\nRESULTADOS")
print("-" * 50)

# Recorrer matriz
for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(
        categoria,
        precio_base,
        categoria_objetivo,
        umbral
    )

    print("Producto:", nombre)
    print("Precio Base:", precio_base)
    print("Precio Final:", precio_final)
    print("-" * 50)