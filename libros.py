class Libro:
    def __init__(self, titulo: str, autor: str, precio: float):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.siguiente = None 

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_libro(self, titulo, autor, precio):
        nuevo_libro = Libro(titulo, autor, precio)
        if not self.cabeza:
            self.cabeza = nuevo_libro
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_libro

    def eliminar_libro(self, titulo):
        actual = self.cabeza
        anterior = None
        while actual and actual.titulo != titulo:
            anterior = actual
            actual = actual.siguiente
        if not actual:
            return False 
        if anterior:
            anterior.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente
        return True

    def obtener_libros(self) -> list[dict]:
        libros = []
        actual = self.cabeza
        while actual:
            libros.append({
                'titulo': actual.titulo,
                'autor': actual.autor,
                'precio': actual.precio
            })  
            actual = actual.siguiente
        return libros
