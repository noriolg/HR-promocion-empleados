
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from variables import *
import plotly.express as px
import utils

# 2. Key variables - How are promotions granted?
# ====================================================


def plot_promotions_by_cat_variable(colname):
    '''Creates a bar chart with the total number of promoted and non promoted people by each of the unique values of the specified column name. 
    These column names should represent categorical variables

        Parameters:
                colname (string):  the unique values of this column of the df will be the bars in the x axis of the plot. Total promotions will be calculated for each.

        Returns:
                fig (go.Figure): figure with the absolute promotions barchart for the specified column
    '''

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

    fig = utils.layout_additions(fig)

    return fig


def plot_percentage_promotions_by_cat_variable(colname):
    '''Creates a bar chart with the distribution of promotion percentages by each of the unique values of the specified column.
    These column names should represent categorical variables

        Parameters:
                colname (string):  the unique values of this column of the df will be the bars in the x axis of the plot. Promotion percentages will be calculated for each

        Returns:
                fig (go.Figure): figure with the promotion percentage barchart for the specified column
    '''

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
    fig = utils.layout_additions(fig)
    return fig


def plot_promotions_by_quant_variable(colname):
    '''Creates a histrogram with the total number of promoted and non promoted people by each of the unique values of the specified column name. 
    These column names should represent categorical variables

        Parameters:
                colname (string):  the unique values of this column of the df will be the bars in the x axis of the plot. Total promotions will be calculated for each.

        Returns:
                fig (go.Figure): figure with the absolute promotions histogram for the specified column
    '''

    trace0 = go.Histogram(x=df[df["is_promoted"] == 1][colname],
                          name="Promoted",
                          marker_color="mediumspringgreen",
                          opacity=0.7)

    trace1 = go.Histogram(x=df[df["is_promoted"] == 0][colname],
                          name="Not Promoted",
                          marker_color="salmon",
                          opacity=0.7)

    data = [trace0, trace1]
    layout = go.Layout(title="Promotions by " +
                       dict_of_column_names[colname], xaxis_title=dict_of_column_names[colname], yaxis_title="Frequency", paper_bgcolor="#FAF9F9")
    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig


def plot_percentage_promotions_by_quant_variable(colname):
    '''Creates a histogram with the distribution if promotion percentages by each of the unique values of the specified column.
    These column names should represent quantitative variables

        Parameters:
                colname (string):  the unique values of this column of the df will be the bars in the x axis of the plot. Promotion percentages will be calculated for each

        Returns:
                fig (go.Figure): figure with the promotion percentage histogram for the specified column
    '''

    totals_per_col = df[colname].value_counts()

    # Quita los NAs de los valores únicos
    unique_values = df[colname].unique()[~np.isnan(df[colname].unique())]

    # Se obtienen los porcentajes.
    percentages = [df[(df[colname] == item) & (df['is_promoted'] == 1)]
                   [colname].count()/totals_per_col[item] for item in unique_values]
    names = unique_values
    # Los "names" están en el orden de aparición de la variable en colname

    # Las categorías se ordenan por orden de los "names" para que aparezcan ordenados
    df_percentages = pd.DataFrame()
    df_percentages['names'] = names
    df_percentages['percentages'] = percentages
    df_percentages.sort_values(by="names", inplace=True)

    xnames = df_percentages['names']
    if len(names) < 10:
        # Si quiero que se vean todos, lo transformo a string
        xnames = [str(number) for number in xnames]

    trace0 = go.Bar(x=xnames,
                    y=df_percentages['percentages'],
                    name="Promoted",
                    marker_color="mediumspringgreen",
                    text=["{0}%".format(round(value*100, 1))
                          for value in df_percentages['percentages']],
                    textposition="auto",
                    textangle=0,
                    textfont_size=20,
                    textfont_color="black",
                    )

    data = [trace0]
    layout = go.Layout(title="% Promotions by " +
                       dict_of_column_names[colname], xaxis_title=dict_of_column_names[colname], yaxis_title="% of workers", paper_bgcolor="#FAF9F9")
    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig


# STATIC PLOTS
# ==============================
def department_constitution(title):
    '''Creates a static bubble plot showing department size, average % promotions and aberage previous year rating

        Parameters:
                title (string):  title to be shown in the plot

        Returns:
                fig (go.Figure): figure with the described plot
    '''

    traces = [go.Scatter(x=df_department[df_department['department'] == department]['percentage_promotions'],
                         y=df_department[df_department['department']
                                         == department]['mean_prev_year_rating'],
                         mode='markers',
                         marker_size=df_department[df_department['department']
                                                   == department]['total_people']/100,
                         hovertemplate='<b>{0}</b><br><br>'.format(department) +
                         '<b>T. People:</b> {0}<br>'.format(df_department[df_department['department'] == "HR"]['total_people'].values[0]) +
                         '<b>Promotion:</b> {0}%<br>'.format(round(df_department[df_department['department'] == department]['percentage_promotions'].values[0]*100, 2)) +
                         '<b>Y. Ranking:</b> %{y:.1f}<br>',
                         showlegend=False,
                         name=''
                         ) for department in df_department['department']]

    data = traces
    layout = go.Layout(title=title, xaxis_title="% of promotions",
                       yaxis_title="Prev. year rating", paper_bgcolor="#FAF9F9")

    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig


def ages_service_lengths(title):
    '''Creates a static bubble plot showing promotion percentage (size) and number of workers (color) for every age and length of service

        Parameters:
                title (string):  title to be shown in the plot

        Returns:
                fig (go.Figure): figure with the described plot
    '''

    ages_labels = [
        "Age: " + str(x) + "   " for x in df_ages_service_lengths["age"]]
    length_labels = [
        "L. Serv: " + str(x) + "   " for x in df_ages_service_lengths["length_of_service"]]
    percentage_labels = ["Promotion perc. : " + str(x) + "%" for x in round(
        df_ages_service_lengths["per_promoted"]*100, 1).values]

    text_labels = []
    for i in range(len(ages_labels)):
        text_labels.append(
            ages_labels[i] + length_labels[i] + percentage_labels[i])

    trace0 = go.Scatter(x=df_ages_service_lengths["age"],
                        y=df_ages_service_lengths["length_of_service"],
                        mode="markers",
                        showlegend=False,
                        marker={
                            "color": df_ages_service_lengths['tot_people'],
                            "size": df_ages_service_lengths["per_promoted"]*50,
                            "showscale": True,
                            "cmax": 100,
                            "cmin": 0,
                            "colorbar": {
                                "title": "Number of workers in group"
                            },
                            "colorscale": "plasma"
    },
        text=text_labels,
        hovertemplate="%{text}",
        name=" "

    )

    data = [trace0]
    layout = go.Layout(title=title,
                       xaxis_title="Age", yaxis_title="Length of service", paper_bgcolor="#FAF9F9")

    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig


def avg_training_score_no_of_trainings_promotions(title):
    '''Creates a static scatter plot showing promotion percentage by average training score and number of trainings

        Parameters:
                title (string):  title to be shown in the plot

        Returns:
                fig (go.Figure): figure with the described plot
    '''

    fig = px.scatter(df, x="avg_training_score", y="no_of_trainings",
                     color="is_promoted",
                     labels={
                         "avg_training_score": dict_of_column_names["avg_training_score"],
                         "no_of_trainings": dict_of_column_names["no_of_trainings"],
                         "is_promoted": dict_of_column_names["is_promoted"]
                     },
                     title=title)
    fig = utils.layout_additions(fig)
    return fig


def department_avg_training_score(title):
    '''Creates a static box plot showing average training score broken down by department and promotion

        Parameters:
                title (string):  title to be shown in the plot

        Returns:
                fig (go.Figure): figure with the described plot
    '''

    fig = px.box(df, x="department", y="avg_training_score",
                 color="is_promoted",
                 title=title,
                 labels={
                     "department": dict_of_column_names["department"],
                     "avg_training_score": dict_of_column_names["avg_training_score"],
                     "is_promoted": dict_of_column_names["is_promoted"]
                 },
                 color_discrete_sequence=['salmon', "mediumspringgreen"],
                 )
    newnames = {"0": 'Not Promoted', "1": 'Promoted'}
    fig.for_each_trace(lambda t: t.update(name=newnames[t.name]))
    fig.update_traces(quartilemethod="exclusive")
    fig = utils.layout_additions(fig)
    return fig


# Is the company an equal opportunity employer?
def distribution_of_workers_per_department_and_gender_percentages(title):
    '''Creates a static bar plot showing gender distribution by department

        Parameters:
                title (string):  title to be shown in the plot

        Returns:
                fig (go.Figure): figure with the described plot
    '''

    trace0 = go.Bar(x=df_department['department'], y=df_department['male_staff'] /
                    df_department['total_people'], name="Male Staff")
    trace1 = go.Bar(x=df_department['department'], y=df_department['female_staff'] /
                    df_department['total_people'], name="Female Staff")

    data = [trace0, trace1]
    layout = go.Layout(title=title, yaxis_title="Percentage of workers",
                       showlegend=False)  # We do not show the legend because it is shown in the plot in the right
    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)

    return fig


def distribution_of_workers_per_department_and_gender_absolutes(title):
    '''Creates a static bar plot showing absolute numbers for gender distribution by department

        Parameters:
                title (string):  title to be shown in the plot

        Returns:
                fig (go.Figure): figure with the described plot
    '''

    trace0 = go.Bar(x=df_department['department'],
                    y=df_department['male_staff'], name="Male Staff")
    trace1 = go.Bar(x=df_department['department'],
                    y=df_department['female_staff'], name="Female Staff")

    data = [trace0, trace1]
    layout = go.Layout(title=title,
                       yaxis_title="Number of workers")
    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig


def distribution_of_workers_promotion_per_department_and_gender(title):
    '''Creates a static bar plot showing percentage of workers promoted by department and gender

        Parameters:
                title (string):  title to be shown in the plot

        Returns:
                fig (go.Figure): figure with the described plot
    '''

    trace0 = go.Bar(x=df_department['department'], y=df_department['promotions_male_staff'] /
                    df_department['male_staff'], name="Male Staff")
    trace1 = go.Bar(x=df_department['department'], y=df_department['promotions_female_staff'] /
                    df_department['female_staff'], name="Female Staff")

    data = [trace0, trace1]
    layout = go.Layout(title=title, xaxis_title="Department",
                       yaxis_title="Percentage of workers promoted", showlegend=False)  # We do not show the legend because it is shown in the plot above
    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig


def total_distribution_of_workers_promotion(title):
    '''Creates a static bar plot showing aggregate percentage of workers promoted by gender

        Parameters:
                title (string):  title to be shown in the plot

        Returns:
                fig (go.Figure): figure with the described plot
    '''

    trace0 = go.Bar(y=['Male', 'Female'], x=[df_department['promotions_male_staff'].sum()/df_department['male_staff'].sum(),
                    df_department['promotions_female_staff'].sum()/df_department['female_staff'].sum()], name="Staff", orientation='h')

    data = [trace0]
    layout = go.Layout(title=title, xaxis_title="Percentage of workers promoted",
                       yaxis_title="Gender", showlegend=False)  # We do not show the legend because it is shown in the plot above
    fig = go.Figure(data=data, layout=layout)
    fig = utils.layout_additions(fig)
    return fig
