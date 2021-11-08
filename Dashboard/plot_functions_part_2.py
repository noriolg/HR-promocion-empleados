
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from variables import *


# 2. Key variables - How are promotions granted?
# ====================================================
def plot_promotions_by_cat_variable(colname):
    trace0 = go.Bar(x=df[colname].unique(),
                    y=[df[(df[colname] == item) & (df['is_promoted'] == 1)]
                       [colname].count() for item in df[colname].unique()],
                    name="Promoted",
                    marker_color="mediumspringgreen")

    trace1 = go.Bar(x=df[colname].unique(),
                    y=[df[(df[colname] == item) & (df['is_promoted'] == 0)]
                       [colname].count() for item in df[colname].unique()],
                    name="Not Promoted",
                    marker_color="salmon")

    data = [trace0, trace1]
    layout = go.Layout(title="Promotions by " + dict_of_column_names[colname],
                       xaxis_title=dict_of_column_names[colname], yaxis_title="Number of workers", paper_bgcolor="#FAF9F9")
    fig = go.Figure(data=data, layout=layout)
    return fig


def plot_percentage_promotions_by_cat_variable(colname):

    totals_per_col = df[colname].value_counts()
    unique_values = df[colname].unique()

    y = [df[(df[colname] == item) & (df['is_promoted'] == 1)]
         [colname].count()/totals_per_col[item] for item in unique_values]
    trace0 = go.Bar(x=df[colname].unique(),
                    y=y,
                    name="Promoted",
                    marker_color="mediumspringgreen",
                    text=["{0}%".format(round(value*100, 1)) for value in y],
                    textposition="auto",
                    textangle=0,
                    textfont_size=20,
                    textfont_color="black",
                    )

    data = [trace0]
    layout = go.Layout(title="% Promotions by " +
                       dict_of_column_names[colname], xaxis_title=dict_of_column_names[colname], yaxis_title="% of workers", paper_bgcolor="#FAF9F9")
    fig = go.Figure(data=data, layout=layout)
    return fig


def secure_plot_percentage_promotions_by_cat_variable(colname, df):
    # Guardamos la base de datos en una variable auxiliar
    df_aux = df.copy()
    # Rellenamos los NA para mostrarlos
    df[colname].fillna(value="NA", inplace=True)
    # Se muestra
    fig = plot_percentage_promotions_by_cat_variable(colname)
    # Se recupera la base de datos inicial
    df = df_aux.copy()
    return fig
