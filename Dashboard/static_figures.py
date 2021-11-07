import pandas as pd
import numpy as np
import plotly.graph_objects as go


df = pd.read_csv('data/trabajo1.csv')


df_reduced = df.iloc[0:500, :].copy()
initial_table = go.Figure(data=[go.Table(
    columnwidth=[15]*(len(list(df.columns))-1),
    header=dict(values=["Department", "Region", "Education", "Gender", "Recruitment", "Nº Trainings", "Age", "Rating", "Nº Years", "Nº Awards", "Tr. Score", "Promoted"],
                fill_color='grey',
                align=['left', 'center'],
                font=dict(color='white', size=8)
                ),

    cells=dict(values=[df_reduced.department, df_reduced.region, df_reduced.education, df_reduced.gender, df_reduced.recruitment_channel, df_reduced.no_of_trainings, df_reduced.age, df_reduced.previous_year_rating, df_reduced.length_of_service, df_reduced.awards_won, df_reduced.avg_training_score, df_reduced.is_promoted],
               fill_color=[["white", "lightgrey"]*int(df_reduced.shape[0]/2)],
               align=['left', 'center'],
               font=dict(color='darkslategray', size=6),
               ),
)
],  layout=go.Layout(paper_bgcolor="#FAF9F9"))
