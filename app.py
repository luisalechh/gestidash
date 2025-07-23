import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State

from layout.sidebar import get_sidebar, CONTENT_STYLE
from pages import home, page1, page2

# Inicializa la app con tema Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "GestiDASH"
server = app.server  # si luego deseas desplegarlo en Heroku o similar

# Navbar superior con botón para abrir el menú
navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
            dbc.Col(
                dbc.Button("☰", id="open-sidebar", n_clicks=0, color="secondary", className="me-2"),
                width="auto",
                style={"padding-left": "0px", "margin-left": "0px"}
            ),
            dbc.Col(
                html.H2("GestiDash", className="navbar-brand mb-0"),
                style={"display": "flex", "align-items": "center"}
            )
        ], align="center", className="g-0", style={"margin-left": "0px", "padding-left": "0px"})
    ],
    fluid=True),
    color="dark",
    dark=True,
    className="mb-4"
)


# Layout general de la app
app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    get_sidebar(),  # sidebar responsive
    html.Div(id="page-content", style=CONTENT_STYLE),
])

# Callback para mostrar u ocultar el menú lateral
@app.callback(
    Output("offcanvas-sidebar", "is_open"),
    Input("open-sidebar", "n_clicks"),
    State("offcanvas-sidebar", "is_open")
)
def toggle_offcanvas(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# Callback para cambiar el contenido de la página
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/onboarding":
        return page1.layout
    elif pathname == "/cuentas-bancarias":
        return page2.layout
    return html.Div([
        html.H1("404: Página no encontrada", className="text-danger"),
        html.Hr(),
        html.P(f"La ruta {pathname} no fue reconocida."),
    ], className="p-3 bg-light rounded-3")

if __name__ == "__main__":
    app.run(debug=True, port=8888)
