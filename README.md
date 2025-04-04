# DebTechnical

## Descripción
DebTechnical es una aplicación basada en FastAPI que simula la gestión de una tienda en línea. Permite registrar usuarios, agregar productos, gestionar carritos de compras y finalizar compras, todo utilizando reglas de precios personalizadas para calcular los totales.

## Pasos para la instalación
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/DAD-GEEK/DebTechnical.git
   cd DebTechnical
   ```

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install "fastapi[standard]"
   pip install uvicorn
   ```

4. **Ejecutar la aplicación**:
   ```bash
   uvicorn main:app --reload
   ```
   como ya esta configuradoel ambiente en vscode puede seleccionar run por el launch.json

## Endpoints disponibles

### Salud del sistema
- **GET /health/**  
  Verifica que la API esté funcionando correctamente.  
  **Respuesta**: `{"status": "Hello Robot!"}`

### Gestión de usuarios
- **POST /usuario/**  
  Registra un nuevo usuario.  
  **Parámetros**: `nombre: str`  
  **Respuesta**: Usuario registrado.

- **GET /usuarios**  
  Obtiene la lista de todos los usuarios registrados.  
  **Respuesta**: Lista de usuarios.

### Gestión de productos
- **POST /producto/**  
  Agrega un nuevo producto a la tienda.  
  **Parámetros**: `sku: str`, `nombre: str`, `descripcion: str`, `unidades: int`, `precio: float`  
  **Respuesta**: Producto agregado.

- **GET /productos**  
  Obtiene la lista de todos los productos disponibles en la tienda.  
  **Respuesta**: Lista de productos.

### Gestión del carrito
- **POST /anadirCarrito**  
  Añade un producto al carrito de un usuario.  
  **Parámetros**: `usuario_nombre: str`, `skuproducto: str`, `cantidad: int`  
  **Respuesta**: Carrito actualizado o error.

- **DELETE /eliminarProductCarrito**  
  Elimina un producto del carrito de un usuario.  
  **Parámetros**: `usuario_nombre: str`, `skuproducto: str`  
  **Respuesta**: Carrito actualizado o error.

- **GET /user/carrito**  
  Obtiene el carrito de un usuario.  
  **Parámetros**: `usuario_nombre: str`  
  **Respuesta**: Detalles del carrito o error.

### Finalización de compra
- **POST /finalizarCompra**  
  Finaliza la compra de un usuario, descontando las unidades del inventario y vaciando el carrito.  
  **Parámetros**: `usuario_nombre: str`  
  **Respuesta**: Total de la compra y detalles del carrito.

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.