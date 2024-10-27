import reflex as rx
from rxconfig import config
from finalda.libros import ListaEnlazada, Libro

lista_libros = ListaEnlazada()


class BookState(rx.State):
    current_title: str = ""
    current_author: str = ""
    current_price: float = 0.0

    @rx.var
    def book_list(self) -> list[dict]:
        return lista_libros.obtener_libros()

    def add_book(self):
        """Agrega un nuevo libro a la lista enlazada."""
        lista_libros.agregar_libro(self.current_title, self.current_author, self.current_price)
        self.current_title = ""
        self.current_author = ""
        self.current_price = 0.0

    def remove_book(self, title: str):
        lista_libros.eliminar_libro(title)


def render_book(book):
    return rx.hstack(
        rx.text(
            f"Título: {book['titulo']} - Autor: {book['autor']} - Precio: ${book['precio']:.2f}",
            font_size="18px",
            color="lightgray",
            padding="8px",
        ),
        rx.button(
            "Eliminar",
            on_click=lambda: BookState.remove_book(book['titulo']),
            background_color="#ff1744",
            color="white",
            padding="8px",
            border_radius="5px",
            _hover={"background_color": "#d50000"}
        ),
        justify="space-between",
        align="center",
        padding="10px",
        border_bottom="1px solid #333"
    )


def index():
    return rx.vstack(
        # Encabezado de bienvenida
        rx.heading(
            "Bienvenido a LibroHub!",
            font_size="32px",
            color="white",
            padding="10px",
        ),

        # Formulario para agregar un libro
        rx.input(
            placeholder="Título del libro",
            on_change=BookState.set_current_title,
            padding="10px",
            border="1px solid #444",
            border_radius="5px",
            width="100%",
            margin_bottom="10px",
            background_color="#333",
            color="white"
        ),
        rx.input(
            placeholder="Autor del libro",
            on_change=BookState.set_current_author,
            padding="10px",
            border="1px solid #444",
            border_radius="5px",
            width="100%",
            margin_bottom="10px",
            background_color="#333",
            color="white"
        ),
        rx.input(
            placeholder="Precio del libro",
            type="number",
            on_change=BookState.set_current_price,
            padding="10px",
            border="1px solid #444",
            border_radius="5px",
            width="100%",
            margin_bottom="10px",
            background_color="#333",
            color="white"
        ),
        rx.button(
            "Agregar libro",
            on_click=BookState.add_book,
            background_color="#1e88e5",
            color="white",
            padding="12px",
            border_radius="5px",
            font_weight="bold",
            _hover={"background_color": "#0d47a1"},
            margin_bottom="20px"
        ),

        rx.foreach(BookState.book_list, render_book),

        padding="20px",
        max_width="600px",
        margin="0 auto",
        box_shadow="0px 4px 8px rgba(0, 0, 0, 0.3)",
        border_radius="8px",
        background_color="#212121",
    )


# Configuración de la aplicación
app = rx.App()
app.add_page(index)
