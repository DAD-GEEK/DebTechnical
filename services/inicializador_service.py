
from services.tienda_service import TiendaService
import random


tienda_service = TiendaService()

class inicializador_service:
    def inicializador(self):
        usuarios = ["Marcela", "Paula", "Isabella", "Alejandro", "Pepito Perez"]
        for usuario in usuarios:
            tienda_service.registrar_usuario(usuario)
            print(f"Usuario registrado: {usuario}")
        print("Usuarios registrados exitosamente.")
        
        productos = [
            {"sku": f"{random.choice(['EA', 'WE', 'SP'])}{i:03}", 
            "nombre": nombre, 
            "descripcion": descripcion, 
            "unidades": random.randint(1, 50), 
            "precio": round(random.uniform(1.0, 50.0), 2)}
            for i, (nombre, descripcion) in enumerate([
                ("Arroz", "Grano básico"), 
                ("Frijoles", "Legumbre seca"), 
                ("Aceite", "Aceite vegetal"), 
                ("Azúcar", "Endulzante"), 
                ("Sal", "Condimento esencial"), 
                ("Harina", "Base para pan"), 
                ("Leche", "Lácteo líquido"), 
                ("Huevos", "Proteína básica"), 
                ("Pan", "Producto horneado"), 
                ("Café", "Bebida estimulante"), 
                ("Té", "Infusión caliente"), 
                ("Mantequilla", "Grasa láctea"), 
                ("Queso", "Lácteo sólido"), 
                ("Pollo", "Carne blanca"), 
                ("Carne de res", "Carne roja"), 
                ("Pescado", "Proteína marina"), 
                ("Pasta", "Base para comidas"), 
                ("Tomates", "Vegetal fresco"), 
                ("Cebollas", "Vegetal aromático"), 
                ("Papas", "Tubérculo básico"), 
                ("Zanahorias", "Vegetal dulce"), 
                ("Manzanas", "Fruta fresca"), 
                ("Plátanos", "Fruta tropical"), 
                ("Naranjas", "Fruta cítrica"), 
                ("Uvas", "Fruta pequeña"), 
                ("Yogur", "Lácteo fermentado"), 
                ("Cereal", "Desayuno rápido"), 
                ("Jabón", "Producto de limpieza"), 
                ("Detergente", "Limpieza de ropa"), 
                ("Papel higiénico", "Uso personal")
            ], start=1)
        ]
        for producto in productos:
            tienda_service.agregar_producto(**producto)
        print("Productos agregados exitosamente.")

        return tienda_service.tienda
