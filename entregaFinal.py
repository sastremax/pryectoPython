from rich.console import Console
from rich.table import Table
import sqlite3

console = Console()

# Funcion para copnectarse a la Base de Datos
def obtener_conexion():
    return sqlite3.connect("inventario.db")

def crear_base_y_tabla():

    # Apertura de la conexion con la Base de Datos
    conexion= obtener_conexion()

    # Creacion del cursor
    cursor = conexion.cursor()

    # Creacion de la base de datos y la tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    # Guardado de cambios
    conexion.commit()

    # Cerramos la conexión con el cursor
    cursor.close()

# Mostrar los productos desde la base de datos
def mostrar_productos():
    conexion= obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        console.print("❌ No hay productos en la base de datos.", style="bold red")
        return

    table = Table(title="📋 LISTADO DE PRODUCTOS")
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nombre", style="magenta")
    table.add_column("Stock", justify="right", style="green")

    for producto in productos:
        table.add_row(str(producto[0]), producto[1], str(producto[2]))

    console.print(table)

# cargando datos para los productos
def agregar_producto():
    console.print("📝 [cyan]Agregando productos...[/cyan]\n")
    nombre_producto = input("Ingrese el nombre del producto: ").lower()

    while True:
        nuevo_stock = input("Ingrese la cantidad de stock: ")
        if int(nuevo_stock) > 0:
            nuevo_stock = int(nuevo_stock)
            break
        console.print("❌ [bold red]El stock debe ser un número mayor a 0.[/bold red]")

    conexion= obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (nombre, stock) VALUES (?, ?)", (nombre_producto, nuevo_stock))
    conexion.commit()
    conexion.close()

    console.print(f"✅ El producto '[bold green]{nombre_producto}[/bold green]' fue agregado con {nuevo_stock} unidades.")

# actualizando los productos
def actualizar_producto():
    console.print("✏️ [yellow]Actualizando el stock de un producto[/yellow]\n")
    id_producto = input("Ingrese el ID del producto a actualizar: ")

    while True:
        nuevo_stock = input("Ingrese el nuevo stock: ")
        if int(nuevo_stock) > 0:
            nuevo_stock = int(nuevo_stock)
            break
        console.print("❌ [bold red]El stock debe ser un número mayor a 0.[/bold red]")

    conexion= obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (nuevo_stock, id_producto))
    if cursor.rowcount > 0:
        console.print(f"✅ Stock del producto con ID {id_producto} actualizado a {nuevo_stock} unidades.")
    else:
        console.print("❌ [bold red]No se encontró un producto con ese ID.[/bold red]")
    conexion.commit()
    conexion.close()

# eliminando los productos
def eliminar_producto():
    console.print("🗑️ [red]Eliminando un producto...[/red]\n")
    nombre_producto = input("Ingrese el nombre del producto a eliminar: ").lower()

    conexion= obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos WHERE LOWER(nombre) = ?", (nombre_producto,))
    producto = cursor.fetchone()

    if producto:
        cursor.execute("DELETE FROM productos WHERE LOWER(nombre) = ?", (nombre_producto,))
        conexion.commit()
        console.print(f"✅ El producto '[bold green]{nombre_producto}[/bold green]' fué eliminado correctamente.")
    else:
        console.print(f"❌ [bold red]No se encontró un producto llamado '{nombre_producto}'.[/bold red]")

    conexion.close()

# buscando un producto por nombre
def buscar_producto_por_nombre():
    console.print("🔍 [cyan]Buscando un producto por nombre...[/cyan]\n")
    nombre_producto = input("Ingrese el nombre del producto a buscar: ").lower()

    conexion= obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE LOWER(nombre) = ?", (nombre_producto,))
    producto = cursor.fetchone()
    conexion.close()

    if producto:
        console.print("\n✅ [bold green]Producto encontrado:[/bold green]")
        console.print(f"ID: {producto[0]} | Nombre: {producto[1]} | Stock: {producto[2]}")
    else:
        console.print(f"❌ [bold red]El producto '{nombre_producto}' no fue encontrado.[/bold red]")

# buscando un producto por precio con tope
def buscar_producto_por_precio_tope():
    console.print("🔍 [cyan]REPORTE DE PRODUCTOS POR PRECIO CON TOPE A ELECCION...[/cyan]\n")
    while True:
        tope_precio = input("Ingrese el precio máximo de los productos a buscar: ")
        if int(tope_precio) > 0:
            tope_stock = int(tope_precio)
            break
        console.print("❌ [bold red]El precio debe ser un número positivo.[/bold red]")

    conexion= obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE stock <= ?", (tope_precio,))
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        table = Table(title=f"📋 Los productos con precio menor o igual a {tope_precio} son: ")
        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Nombre", style="magenta")
        table.add_column("Stock", justify="right", style="green")

        for producto in productos:
            table.add_row(str(producto[0]), producto[1], str(producto[2]))
        console.print(table)
    else:
        console.print(f"❌ [bold red]No hay productos con precios menor o igual a {tope_precio}.[/bold red]")

# reportando bajo stock
def reportar_bajo_stock():
    console.print("⚠️ [yellow]Reporte de productos con bajo stock...[/yellow]\n")
    limite_stock = int(input("Ingrese el límite de stock para el reporte: "))

    conexion= obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE stock <= ?", (limite_stock,))
    productos = cursor.fetchall()
    conexion.close()

    if not productos:
        console.print("✅ [bold green]No hay productos con bajo stock.[/bold green]")
        return

    table = Table(title=f"⚠️ Productos con stock menor o igual a {limite_stock}")
    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Nombre", style="magenta")
    table.add_column("Stock", justify="right", style="green")

    for producto in productos:
        table.add_row(str(producto[0]), producto[1], str(producto[2]))

    console.print(table)

# buscando producto por ID
def mostrar_producto_por_id():
    console.print("🔍 [cyan]Buscando un producto por ID...[/cyan]\n")
    id_producto = input("Ingrese el ID del producto: ")

    # Conectar a la base de datos y buscar por ID
    conexion= obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    conexion.close()

    if producto:
        # Mostrar el producto encontrado
        console.print("\n✅ [bold green]Producto encontrado:[/bold green]")
        table = Table()
        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Nombre", style="magenta")
        table.add_column("Stock", justify="right", style="green")
        table.add_row(str(producto[0]), producto[1], str(producto[2]))
        console.print(table)
    else:
        console.print(f"❌ [bold red]No se encontró un producto con el ID '{id_producto}'.[/bold red]")

# salir
def salir():
    console.print("\n👋 [bold cyan]Hasta luego! Vuelve pronto!!![/bold cyan]\n")

# Menú principal
console.print("\n[bold cyan]BIENVENIDO/A! 😊 A LA TIENDA DE ROPA CODERCLOTHES[/bold cyan]\n")
def menu_principal():
    console.print("[bold cyan]MENU:[/bold cyan]\n")
    console.print(" 1  -  📝 [green]AGREGAR PRODUCTOS A LA TIENDA[/green]")
    console.print(" 2  -  📋 [cyan]MOSTRAR TODOS LOS PRODUCTOS[/cyan]")
    console.print(" 3  -  📋️️ [cyan]MOSTRAR PRODUCTO POR ID[cyan]")
    console.print(" 4  -  ✏️ [yellow]ACTUALIZAR EL STOCK DE UN PRODUCTO[/yellow]")
    console.print(" 5  -  🗑️ [red]ELIMINAR PRODUCTOS[/red]")
    console.print(" 6  -  🔍 [cyan]BUSCAR PRODUCTO POR NOMBRE[/cyan]")
    console.print(" 7  -  🔍️ [cyan]BUSCAR PRODUCTOS POR PRECIO (con tope)[/cyan]")
    console.print(" 8  -  ⚠️️ [yellow]REPORTE DE BAJO STOCK[/yellow]")
    console.print(" 0  -  👋 [white]SALIR[/white]\n")
    return input("Ingrese una opción: ")

crear_base_y_tabla()
opcion = ""
while opcion != "0":
  opcion = menu_principal()
  if opcion == "1":
    agregar_producto()
  elif opcion == "2":
    mostrar_productos()
  elif opcion == "3":
    mostrar_producto_por_id()
  elif opcion == "4":
      actualizar_producto()
  elif opcion == "5":
      eliminar_producto()
  elif opcion == "6":
      buscar_producto_por_nombre()
  elif opcion == "7":
      buscar_producto_por_precio_tope()
  elif opcion == "8":
      reportar_bajo_stock()
  elif opcion == "0":
    salir()
  else:
    print("❌ La opción elegida es incorrecta. Intentelo nuevamente.")