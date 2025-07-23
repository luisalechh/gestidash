import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Datos base
df = pd.DataFrame({
    "Sistemas": ["Gestisaf", "Extranet"],
    "N° de registros": [6000, 1000]
})


df_status = pd.DataFrame({
    "N° de registros": [6580, 1596],
    "Estado": ["Aprobado","Pendiente"]
})

# Valor de ejemplo: cantidad de clientes
cantidad_clientes = 1583
cantidad_clientes_hoy = 4
cantidad_clientes_aprobados_hoy = 2

colores_personalizados = ["#5ec6be", "#337ab7"]  # Azul Bootstrap + Morado Bootstrap


# Gráfico de barras horizontales (card 1)
bar_horizontal = px.bar(
    df, x="N° de registros", y="Sistemas", color="Sistemas",orientation="h", title="",
    color_discrete_sequence=colores_personalizados
)
bar_horizontal.update_layout(margin=dict(l=40, r=20, t=40, b=40))

# Gráfico de torta (card 2)
pie_chart = px.pie(df_status, names="Estado", values="N° de registros", title="",
    color_discrete_sequence=colores_personalizados)
pie_chart.update_traces(textinfo="percent+label")
pie_chart.update_layout(margin=dict(l=40, r=20, t=40, b=40))

# Gráfico de barras verticales (card 3)
bar_vertical = px.bar(df, x="Sistemas", y="N° de registros", title="")
bar_vertical.update_layout(margin=dict(l=40, r=20, t=40, b=40))



# Card 1 - Barras horizontales
first_card = dbc.Card(
    dbc.CardBody([
        html.H5("N° de Registros por Sistema", className="card-title"),
        dcc.Graph(figure=bar_horizontal, config={"displayModeBar": False})
    ]),
    className="text-center shadow mt-5",  # sombra de Bootstrap
)

# Card 2 - Gráfico de torta
second_card = dbc.Card(
    dbc.CardBody([
        html.H5("% Clientes Aprobados", className="card-title"),
        dcc.Graph(figure=pie_chart, config={"displayModeBar": False})
    ]),
    className="text-center shadow mt-5",  # sombra de Bootstrap
)

# Card 3 - Barras verticales
third_card = dbc.Card(
    dbc.CardBody([
        html.H5("Card 3 - Barras Verticales", className="card-title"),
        dcc.Graph(figure=bar_vertical, config={"displayModeBar": False})
    ]),
    className="text-center shadow",  # sombra de Bootstrap
)

# Card 4 - Total de clientes
fourth_card = dbc.Card(
    dbc.CardBody([
        html.H5("Total de Clientes", className="card-title"),
        html.H1(f"{cantidad_clientes:,}", className="display-4", style={"color": "#17a2b8"})
    ]),
    className="text-center shadow mb-5",  # sombra de Bootstrap
)
# Card 5 - Clientes registrados hoy
five_card = dbc.Card(
    dbc.CardBody([
        html.H5("Clientes registrados hoy", className="card-title"),
        html.H1(f"{cantidad_clientes_hoy:,}", className="display-4", style={"color": "#17a2b8"})
    ]),
    className="text-center shadow mb-5",  # sombra de Bootstrap
)

# Card 6 - Clientes aprobado hoy
six_card = dbc.Card(
    dbc.CardBody([
        html.H5("Clientes aprobados hoy", className="card-title"),
        html.H1(f"{cantidad_clientes_aprobados_hoy:,}", className="display-4", style={"color": "#17a2b8"})
    ]),
    className="text-center shadow ",  # sombra de Bootstrap
)



# Fila con las 4 cards
cards_row = dbc.Row([
    dbc.Col(fourth_card, xs=12, md=4),
    dbc.Col(five_card, xs=12, md=4),
    dbc.Col(six_card, xs=12, md=4),
])

'''
cards_row2 = dbc.Row([
    dbc.Col(first_card, width=4),
    dbc.Col(second_card, width=4),
    dbc.Col(third_card, width=4)
])
'''
cards_row2 = dbc.Row([
    dbc.Col(first_card, xs=12, md=8),
    dbc.Col(second_card, xs=12, md=4)
])

# Layout principal
layout = html.Div([
    cards_row,
    cards_row2,

])
