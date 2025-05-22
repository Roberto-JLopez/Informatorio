# Crea un programa que calcule el precio final de un producto
# después de 
# aplicar un descuento. Utilizarás funciones para 
# organizar la lógica del programa.

def calcular_precio_final(precio_inicial, descuento):
    return precio_inicial - (precio_inicial * (descuento / 100))


precio_producto = float(input("Ingrese el precio del producto: "))
descuento_producto = float(input("Ingrese el descuento a aplicar: "))
# print(f"El precio final del producto es: {calcular_precio_final(precio_producto, descuento_producto)}")


promedio = calcular_precio_final(precio_producto, descuento_producto)
print(f"lo que tenes que pagar es: {promedio}")