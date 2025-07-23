from dash import html, dcc
import dash_bootstrap_components as dbc

# Estilo para el contenido principal
CONTENT_STYLE = {
    "margin-left": "0",  # ya no dejamos margen fijo
    "margin-right": "0",
    "padding": "2rem 1rem",
}

# Sidebar responsive con Offcanvas
def get_sidebar():
    return dbc.Offcanvas(
        [
            html.Img(src="/assets/logo-gestidash.png", style={"width": "100%", "margin-bottom": "1rem"}),
            html.Hr(),
            dbc.Nav([
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Onboarding", href="/onboarding", active="exact"),
                dbc.NavLink("Cuentas Bancarias", href="/cuentas-bancarias", active="exact"),
            ], vertical=True, pills=True),
        ],
        id="offcanvas-sidebar",
        title="Menú",
        is_open=False,
        placement="start",
        style={"width": "250px"},
    )
