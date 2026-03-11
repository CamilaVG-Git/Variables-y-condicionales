import reflex as rx

SEGURIDAD_SOCIAL = 0.0591
ISR = 0.15
BONIFICACION = 0.10


class State(rx.State):
    sueldo_bruto: str = ""
    otros_descuentos: str = ""

    seguridad_social: float = 0
    impuesto: float = 0
    bonificacion: float = 0
    sueldo_neto: float = 0
    
    def reiniciar(self):
        self.sueldo_bruto = ""
        self.otros_descuentos = ""
        self.seguridad_social = 0
        self.impuesto = 0
        self.bonificacion = 0
        self.sueldo_neto = 0

    def calcular(self):
        sueldo = float(self.sueldo_bruto or 0)
        otros = float(self.otros_descuentos or 0)

        self.seguridad_social = sueldo * SEGURIDAD_SOCIAL
        self.impuesto = sueldo * ISR
        self.bonificacion = sueldo * BONIFICACION

        total_descuentos = self.seguridad_social + self.impuesto + otros

        self.sueldo_neto = sueldo - total_descuentos + self.bonificacion


def index():
    return rx.center(
        rx.vstack(
            rx.heading("Calculadora de Sueldo Neto"),

            rx.input(
                placeholder="Ingrese el sueldo bruto",
                on_change=State.set_sueldo_bruto
            ),

            rx.input(
                placeholder="Ingrese otros descuentos",
                on_change=State.set_otros_descuentos
            ),

            rx.button(
                "Calcular",
                on_click=State.calcular
            ),

            rx.text("Seguridad Social: ", State.seguridad_social),
            rx.text("ISR: ", State.impuesto),
            rx.text("Bonificación: ", State.bonificacion),
            rx.text("Sueldo Neto: ", State.sueldo_neto),

            spacing="4",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index, on_load=State.reiniciar)