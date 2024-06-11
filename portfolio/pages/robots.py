import reflex as rx

@rx.page("/robots.txt", title="robots.txt")
def robots() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.hstack(
                rx.link(
                    rx.heading("😂", size="9"),
                    href="https://referral.hackthebox.com/mz8xH59", underline="none")),
            padding_y="10em",
            font_size="2em",
            text_align="center",
        )
    )