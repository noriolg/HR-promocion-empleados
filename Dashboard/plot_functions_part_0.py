import pandas as pd
import numpy as np
import plotly.graph_objects as go
from variables import *


def table_initial_variables():

    df_reduced = df.iloc[0:500, :].copy()
    initial_table = go.Figure(data=[go.Table(
        columnwidth=[15]*(len(list(df.columns))-1),
        header=dict(values=["Department", "Region", "Education", "Gender", "Recruitment", "Nº Trainings", "Age", "Rating", "Nº Years", "Nº Awards", "Tr. Score", "Promoted"],
                    fill_color='grey',
                    align=['left', 'center'],
                    font=dict(color='white', size=9)
                    ),

        cells=dict(values=[df_reduced.department, df_reduced.region, df_reduced.education, df_reduced.gender, df_reduced.recruitment_channel, df_reduced.no_of_trainings, df_reduced.age, df_reduced.previous_year_rating, df_reduced.length_of_service, df_reduced.awards_won, df_reduced.avg_training_score, df_reduced.is_promoted],
                   fill_color=[["white", "lightgrey"]
                               * int(df_reduced.shape[0]/2)],
                   align=['left', 'center'],
                   font=dict(color='darkslategray', size=8),
                   ),
    )
    ],  layout=go.Layout(paper_bgcolor="#FAF9F9"))
    return initial_table


def bar_chart_of_variable_distribution():
    df_nunique = pd.DataFrame(
        {"column": df.columns, "nunique": df.nunique().values})
    column_names_for_printing = [dict_of_column_names[colname]
                                 for colname in df_nunique["column"]]
    df_nunique["column_names_for_printing"] = column_names_for_printing

    df_nunique = df_nunique[df_nunique['column'] != "employee_id"]

    trace = go.Bar(x=df_nunique["column_names_for_printing"],
                   y=df_nunique["nunique"],
                   text=["{0}".format(value)
                         for value in df_nunique["nunique"]],
                   textposition="auto",
                   textangle=0,
                   textfont_size=15,
                   textfont_color="black",
                   opacity=0.7
                   )

    data = [trace]
    layout = go.Layout(title="Unique values per column",
                       xaxis_title="Variable", yaxis_title="N. Unique Values", paper_bgcolor="#FAF9F9")
    fig = go.Figure(data=data, layout=layout)
    return fig
