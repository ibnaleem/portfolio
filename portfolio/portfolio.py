import reflex as rx
from .pages.pgp import pgp

@rx.page(route="/", title="Shaffan's Portfolio")
def index() -> rx.Component:
    return rx.center()

app = rx.App(theme=rx.theme(appearance="dark", has_background=True, radius="large", accent_color="teal"))
app.add_page(index)
app.add_page(pgp)