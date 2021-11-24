
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from variables import *
import utils


# 1. Data description - Showing current employee patterns
# ====================================================


def createPieChartofColumn(column_name, others_threshold):
    '''Creates a Pie chart with the distribution of a categorical variable. Lowest percentages can be included
    in "others" category. This can be adjusted with entry parameters.

        Parameters:
                column_name (string): name of the column from df to represent in pie chart. 
                others_threshold (float): percentages lower than this threshold will bre grouped into the "Others" category.

        Returns:
                fig (go.Figure): figure with the pie chart for the specified column and threshold.
    '''

    # List with all unique labels in column
    unique_categories = df[column_name].unique()
    # Totals for each of the unique labels
    totals = [df[df[column_name] == category][column_name].count()
              for category in unique_categories]

    # Dataframe with all values
    df_categories = pd.DataFrame()
    df_categories["category"] = unique_categories
    df_categories["total"] = totals
    df_categories["percentages"] = df_categories["total"] / \
        df_categories["total"].sum()
    df_categories["minor_importance"] = 0

    # Se guarda para usar más tarde en cálculo de porcentajes de other
    total_valores = df_categories["total"].sum()

    # Sorted by total
    df_categories.sort_values(by="total", ascending=False, inplace=True)

    # Combine lower percentages
    acum_total = 0
    for row in range(df_categories.shape[0]):
        row_total = df_categories.iloc[row, 1]
        row_percentage = df_categories.iloc[row, 2]
        if row_percentage < others_threshold:
            # Minor importance is set to 1
            df_categories.iloc[row, 3] = 1
            acum_total = acum_total + row_total

    # Only if total categories > 3
    if len(unique_categories) > 3:
        # We delete all rows with minor importance
        df_categories = df_categories[df_categories['minor_importance'] == 0]

        # Append the "Others" row
        row = ["Others", acum_total, acum_total/total_valores, 0]
        df_categories.loc[len(df_categories)] = row

    # Start pie figure
    labels = df_categories["category"]
    values = df_categories["total"]

    trace = go.Pie(labels=labels,
                   values=values,
                   direction="clockwise")
    data = [trace]
    layout = go.Layout(title="Distribution of " +
                       str(dict_of_column_names[column_name]),  paper_bgcolor="#FAF9F9")
    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig


def createHistogramofColumn(column_name):
    '''Creates a histogram with the distribution of a quantitative variable. 

        Parameters:
                column_name (string): name of the column from df to represent in histogram. 

        Returns:
                fig (go.Figure): figure with the histogram for the specified column.
    '''

    trace0 = go.Histogram(x=df[column_name],
                          opacity=0.7)
    data = [trace0]
    layout = go.Layout(title="Distribution of " +
                       dict_of_column_names[column_name], xaxis_title=dict_of_column_names[column_name], yaxis_title="Frequency", paper_bgcolor="#FAF9F9")
    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig
