opcion = ""
# pre-carga de varios productos
productos = [
  ["remera", 100],
  ["pantalon", 50],
  ["zapatillas", 40],
  ["ojotas", 25],
  ["camisa", 75],
  ["vestido", 86],
  ["campera", 42],
  ["zapatos", 11],
  ["blusa", 9],
  ["poncho", 755]
]

print (" BIENVENIDO/A! 😊 A LA TIENDA DE ROPA CODERCLOTHES \n")

# menu interactivo
while opcion != "0" :
  print("""
    MENU:
      1  -  📝 AGREGAR PRODUCTOS A LA TIENDA
      2  -  📋 MOSTRAR LOS PRODUCTOS
      0  -  👋 SALIR
    """) 
  opcion = input("Ingrese una opcion: ")

# cargando datos para los productos
  if opcion == "1":
    print("cargando el producto\n")

# condicional para no repetir el producto
    while True:
      nombre_producto = input("Ingrese el nombre del producto: ") 
      nombre_producto_existe = False
      for producto in productos:
        if producto[0] ==  nombre_producto:
          nombre_producto_existe = True
          print("El producto ya existe. Ingrese un nombre diferente")
          break
      if not nombre_producto_existe:
        break
      
    nuevo_stock = int(input("Ingrese la cantidad de productos que tendra de stock: "))
    while nuevo_stock <= 0:
      print("Cantidad invalida. Ingrese una cantidad correcta de productos que tendra el stock: ")
      nuevo_stock = int(input("Ingrese la cantidad de productos que tendra de stock: "))
    nuevo_producto = [nombre_producto, nuevo_stock]
    productos.append(nuevo_producto)
    print("Gracias!! 😊")

# mostrando los productos
  elif opcion == "2":
    print("******** LISTADO DE PRODUCTOS *********\n")
    if productos:
      for producto in productos:
        print(f"Nombre del producto: {producto[0]} - Stock: {producto[1]}")
    else:
      print("No hay productos")
# salir
  elif opcion == "0":
    print("Hasta luego 👋. Vuelve pronto!!!")  
  else:
    print("Opcion elegida, incorrecta. Intente nuevamente")
