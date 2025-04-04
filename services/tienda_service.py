from models.tienda import Tienda
from models.usuario import Usuario
from models.producto import Producto

class TiendaService:
    def __init__(self):
        self.tienda = Tienda()

    def registrar_usuario(self, nombre):
        usuario = Usuario(nombre)
        self.tienda.usuarios.append(usuario)
        return usuario

    def agregar_producto(self, sku, nombre, descripcion, unidades, precio):
        producto = Producto(sku, nombre, descripcion, unidades, precio)
        self.tienda.productos.append(producto)
        return producto
    
    def anadir_producto_carrito(self, usuario_nombre, skuproducto, cantidad):
        usuario = self.obtener_usuario(usuario_nombre)
        producto= self.obtener_producto(skuproducto)
        if usuario and producto:
                respuesta = self.tienda.agregar_producto_a_carrito(usuario, producto, cantidad)
                print("Producto agregado al carrito")
                return respuesta
        
    def eliminar_producto_carrito(self, usuario_nombre, skuproducto):
        usuario = self.obtener_usuario(usuario_nombre)
        item= self.obtener_item(skuproducto,usuario)
        if self.validar_productoen_carrito(usuario_nombre, skuproducto):
                self.tienda.eliminar_item_de_carrito(usuario, item)
                print("Producto eliminado del carrito")
                return usuario
        else:
            return {"Error": "No se encontró el producto en el carrito"}
        
    def validar_productoen_carrito(self, usuario_nombre, skuproducto):
        usuario = self.obtener_usuario(usuario_nombre)
        if usuario:
            for item in usuario.carrito.items:
                if item.producto.sku == skuproducto:
                    return True
        return False
    
    def obtener_usuario(self, nombre):
        for usuario in self.tienda.usuarios:
            if usuario.nombre == nombre:
                return usuario
        return None
    
    def obtener_producto(self, sku):
        for producto in self.tienda.productos:
            if producto.sku == sku:
                return producto
        return None
    
    def obtener_item(self, sku, usuario):
        for item in usuario.carrito.items:
            if item.producto.sku == sku:
                return item

    