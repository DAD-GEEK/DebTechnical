from fastapi import FastAPI
from services.tienda_service import TiendaService
from services.inicializador_service import inicializador_service


app = FastAPI()
tienda_service = TiendaService()

@app.on_event("startup")
def startup_event():
    tienda_service.tienda = inicializador_service().inicializador()

@app.get("/health/")
def health_check():
    return {"status": "Hello Robot!"}

@app.post("/usuario/")
def registrar_usuario(nombre: str):
    return tienda_service.registrar_usuario(nombre)

@app.post("/producto/")
def agregar_producto(sku: str, nombre: str, descripcion: str, unidades: int, precio: float):
    return tienda_service.agregar_producto(sku, nombre, descripcion, unidades, precio)

@app.get("/usuarios")
def obtener_usuarios():
    return tienda_service.tienda.usuarios


@app.get("/productos")
def obtener_productos():
    return tienda_service.tienda.productos

@app.post("/anadirCarrito")
def realizar_compra(usuario_nombre: str,skuproducto:str, cantidad: int):
    respuesta = tienda_service.anadir_producto_carrito(usuario_nombre, skuproducto, cantidad)
    if respuesta:
        usuario = tienda_service.obtener_usuario(usuario_nombre)
        return usuario
    else:
        return {"error": "No se pudo agregar el producto al carrito"}

@app.delete("/eliminarProductCarrito")
def eliminar_producto_carrito(usuario_nombre: str, skuproducto:str):
    return tienda_service.eliminar_producto_carrito(usuario_nombre, skuproducto)


@app.get("/user/carrito")
def obtener_carrito(usuario_nombre: str):
    usuario = tienda_service.obtener_usuario(usuario_nombre)
    if usuario:
        return usuario
    return {"error": "Usuario no encontrado"}

@app.post("/finalizarCompra")
def finalizar_compra(usuario_nombre: str):
    usuario = tienda_service.obtener_usuario(usuario_nombre)
    if usuario:
        total = tienda_service.tienda.finalizar_compra(usuario)
        return {"message": "Compra finalizada", 
                "carrito": usuario.carrito.items, 
                "total": total}
    return {"error": "Usuario no encontrado"}
