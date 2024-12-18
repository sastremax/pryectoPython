# Tienda de Ropa CODERCLOTHES

Bienvenido al proyecto **"Tienda de Ropa CODERCLOTHES"**, una aplicación para **gestionar productos en una tienda** usando Python, SQLite3 y la biblioteca **Rich** para darle estilo y color a las salidas por consola.

## Características Principales
1. Agregar nuevos productos a la base de datos.
2. Mostrar todos los productos registrados.
3. Buscar productos por su **ID**.
4. Actualizar el stock de un producto existente.
5. Eliminar productos por su **nombre**.
6. Buscar productos por **nombre**.
7. Reportar productos con un **stock menor o igual a un límite**.
8. Buscar productos cuyo **stock sea menor o igual a un tope**.
9. Mensaje de despedida al salir.

Todo esto se maneja a través de un **menú interactivo** con opciones numeradas. 

## Tecnologías Usadas
1. **Python**: Lenguaje de programación principal.
2. **SQLite3**: Base de datos ligera y rápida para almacenar productos.
3. **Rich**: Biblioteca para darle estilo a la consola con colores, tablas y mensajes visualmente atractivos.

## Estructura del Proyecto
### Archivos:
- **`entregaFinal.py`**: Archivo principal con todo el código.
- **`inventario.db`**: Archivo de base de datos SQLite3 donde se almacenan los productos.

## Cómo Funciona
1. **Inicio**: El programa inicia mostrando un menú con opciones numeradas.
2. El usuario ingresa una opción, y el programa ejecuta la función correspondiente.
3. Cada función interactúa con la base de datos y realiza la acción solicitada.
4. El programa sigue ejecutándose hasta que el usuario elige **Salir (0)**.

## Explicación Detallada de Cada Función

### **1. `obtener_conexion()`**
- **Propósito**: Abre una conexión a la base de datos `inventario.db`.
- **Cómo funciona**: 
```python
return sqlite3.connect("inventario.db")
```

### **2. `crear_base_y_tabla()`**
- **Propósito**: Crea la base de datos y la tabla `productos` si no existen.
- **Tabla creada**:
  - `id`: Clave primaria (número autoincremental).
  - `nombre`: Nombre del producto (texto).
  - `stock`: Cantidad de unidades en stock (entero).
- **Ejemplo de ejecución**:
```python
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    stock INTEGER NOT NULL
)
```

### **3. `mostrar_productos()`**
- **Propósito**: Muestra todos los productos existentes en la base de datos en una tabla bonita.
- **Cómo funciona**:
   - Recupera todos los productos con `SELECT *`.
   - Imprime los resultados usando una **tabla estilizada** de `Rich`.
- **Salida Ejemplo**:
```
📋 LISTADO DE PRODUCTOS
+----+---------+-------+
| ID | Nombre  | Stock |
+----+---------+-------+
|  1 | Jeans   |    50 |
|  2 | Camisas |   120 |
+----+---------+-------+
```

### **4. `agregar_producto()`**
- **Propósito**: Permite al usuario agregar un nuevo producto con su **nombre** y **stock**.
- **Validación**: El stock debe ser un número positivo.
- **Ejemplo**:
```python
Ingrese el nombre del producto: jeans
Ingrese la cantidad de stock: 50
✅ El producto 'jeans' fue agregado con 50 unidades.
```

### **5. `actualizar_producto()`**
- **Propósito**: Actualiza el **stock** de un producto buscándolo por su ID.
- **Validación**: Si el producto no existe, muestra un error.
- **Salida Ejemplo**:
```python
Ingrese el ID del producto a actualizar: 1
Ingrese el nuevo stock: 80
✅ Stock del producto con ID 1 actualizado a 80 unidades.
```

### **6. `eliminar_producto()`**
- **Propósito**: Elimina un producto por su **nombre**.
- **Validación**: Si el producto no existe, muestra un error.
- **Salida Ejemplo**:
```python
Ingrese el nombre del producto a eliminar: jeans
✅ El producto 'jeans' fue eliminado correctamente.
```

### **7. `buscar_producto_por_nombre()`**
- **Propósito**: Busca un producto por su **nombre** y lo muestra.
- **Ejemplo**:
```python
Ingrese el nombre del producto a buscar: jeans
✅ Producto encontrado:
ID: 1 | Nombre: jeans | Stock: 50
```

### **8. `buscar_producto_por_precio_tope()`**
- **Propósito**: Muestra productos con **stock menor o igual** a un límite dado.
- **Salida Ejemplo**:
```
📋 Los productos con stock menor o igual a 50 son:
+----+---------+-------+
| ID | Nombre  | Stock |
+----+---------+-------+
|  1 | Jeans   |    50 |
+----+---------+-------+
```

### **9. `reportar_bajo_stock()`**
- **Propósito**: Reporta productos con **bajo stock**.
- **Límite ingresado por el usuario**.
- **Ejemplo**:
```
⚠️ Productos con stock menor o igual a 10:
+----+---------+-------+
| ID | Nombre  | Stock |
+----+---------+-------+
|  2 | Zapatos |    10 |
+----+---------+-------+
```

### **10. `mostrar_producto_por_id()`**
- **Propósito**: Busca y muestra un producto por su **ID**.
- **Ejemplo**:
```python
Ingrese el ID del producto: 2
✅ Producto encontrado:
ID: 2 | Nombre: Camisas | Stock: 120
```

### **11. `salir()`**
- **Propósito**: Muestra un mensaje de despedida y termina el programa.
```python
👋 Hasta luego! Vuelve pronto!!!
```

## Menú Principal
Al ejecutar el programa, verás:
```
MENU:
 1  -  📝 AGREGAR PRODUCTOS A LA TIENDA
 2  -  📋 MOSTRAR TODOS LOS PRODUCTOS
 3  -  📋✨ MOSTRAR PRODUCTO POR ID
 4  -  ✏️ ACTUALIZAR EL STOCK DE UN PRODUCTO
 5  -  🗑️ ELIMINAR PRODUCTOS
 6  -  🔍 BUSCAR PRODUCTO POR NOMBRE
 7  -  🔍️ BUSCAR PRODUCTOS POR PRECIO (con tope)
 8  -  ⚠️ REPORTAR BAJO STOCK
 0  -  👋 SALIR
```

## Ejecución del Programa
1. Asegúrate de tener Python instalado.
2. Instala la biblioteca `rich` con:
   ```bash
   pip install rich
   ```
3. Ejecuta el programa con:
   ```bash
   python entregaFinal.py
   ```
4. Elige una opción del menú.

Maximiliano Sastre
   
