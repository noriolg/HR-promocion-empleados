import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output
from variables import *
from plot_functions_part_0 import *
from plot_functions_part_1 import *
from plot_functions_part_2 import *

###
# This dashboard is built to show the project's progress
# It is divided into 5 sections:
#
# 1. Explaining the aim of the project and showing the initial data
# 2. Showing the different variables and the characteristics of the dataset
# 3. Show how the different variables interact with each other and how they relate with the target variable
# 4. Describe the model development (null treatment, encoding, test and train) and results
# 5. Describe next steps and objective


app = dash.Dash()


app.layout = html.Div([

    html.Div(
        [
            # 0. Explaining the objective and description
            # ============================================

            dcc.Markdown(children=markdown_dashboard_title,
                      style={"text-align": "center",
                             "color": colors['titles'], "font-weight": "bold"}
                         ),

            dcc.Markdown(children=markdown_part_0_title,
                      style={"text-align": "left",
                             "color": colors['subtitles'], }
                         ),

            dcc.Markdown(children=markdown_part_0_text,
                      style={"color": colors['text'], }
                         ),

            # 1. Data description - Showing current employee patterns
            # ====================================================
            html.P(dcc.Markdown(children=markdown_part_1_title,
                      style={"text-align": "left",
                             "color": colors['subtitles'],
                             "margin-top": "50px"}
            )),

            dcc.Markdown(children=markdown_part_1_text,
                         style={"text-align": "left",
                                "color": colors['text'], }
                         ),

            dcc.Graph(
                figure=initial_table,
                id="tabla-inicial",
                style={
                    "display": "block",
                    "height": "400px"}
            ),

            dcc.Markdown(children="The distribution of categorical variables can be seen in the following pie charts:",
                         style={"text-align": "left",
                                "color": colors['text'], }
                         ),


            dcc.Dropdown(
                options=options_categorical_variables,
                placeholder="Selecciona una variable",
                id="categorical-variable-distribution-picker",
                style={
                    "display": "block",
                    "width": "300px",
                    "margin-left": "10px"
                },
                # Valor por defecto el de la primera variable
                value=options_categorical_variables[0]['value']
            ),


            dcc.Graph(
                id="categorical-variable-distribution-graph",
                style={
                    "display": "block"
                }
            ),

            dcc.Markdown(children="The distribution of quantitative variables can be seen in the following histograms:",
                         style={"text-align": "left",
                                "color": colors['text'], }
                         ),

            dcc.Dropdown(
                options=options_quantitative_variables,
                placeholder="Selecciona una variable",
                id="quantitative-variable-distribution-picker",
                style={
                    "display": "block",
                    "width": "300px",
                    "margin-left": "10px"
                },
                # Valor por defecto el de la primera variable
                value=options_quantitative_variables[0]['value']

            ),


            dcc.Graph(
                id="quantitative-variable-distribution-graph",
                style={
                    "display": "block"
                }
            ),



            # 2. Key variables - How are promotions granted?
            # ====================================================
            html.P(dcc.Markdown(children=markdown_part_2_title,
                                style={"text-align": "left",
                                       "color": colors['subtitles'],
                                       "margin-top": "50px"}
                                )),

            dcc.Markdown(children=markdown_part_2_text,
                         style={"text-align": "left",
                                "color": colors['text'], }
                         ),

            dcc.Markdown(children="The distribution of promotions by variable can be seen in the following pie charts:",
                         style={"text-align": "left",
                                "color": colors['text'], }
                         ),

            html.Div(
                children=[
                    dcc.Dropdown(
                        options=options_categorical_variables,
                        placeholder="Selecciona una variable",
                        id="categorical-variable-distribution-of-promotions-picker",
                        style={
                            "display": "block",
                            "width": "300px",
                            "margin-left": "10px"
                        },
                        # Valor por defecto el de la primera variable
                        value=options_categorical_variables[0]['value']
                    ),


                    html.Div(  # Bloque izquierdo
                        children=[
                               dcc.Graph(
                                   id="categorical-variable-distribution-of-promotions-percentages-graph",
                                   style={
                                       "display": "block"
                                   }
                               )],
                        style={
                            "width": "700px",
                            "height": "575px",
                            "display": "inline-block",
                        },
                    ),

                    html.Div(  # Bloque derecho
                        children=[
                               dcc.Graph(
                                   id="categorical-variable-distribution-of-promotions-graph",
                                   style={
                                       "display": "block"
                                   }
                               )],
                        style={
                            "width": "700px",
                            "height": "575px",
                            "display": "inline-block",
                        },
                    ),


                ],
                style={
                    "text-align": "center"
                }
            ),

            dcc.Markdown(children="Now, we will show a few interesting insights that we have found within the dataset:",
                         style={"text-align": "left",
                                "color": colors['text'], }
                         ),



            # 3. Model development - Can we predict promotions?
            # ====================================================
            html.P(dcc.Markdown(children=markdown_part_3_title,
                                style={"text-align": "left",
                                       "color": colors['subtitles'],
                                       "margin-top": "50px"}
                                )),

            # 4. Employee tool - What can I do as an individual employee?
            # ====================================================
            html.P(dcc.Markdown(children=markdown_part_4_title,
                                style={"text-align": "left",
                                       "color": colors['subtitles'],
                                       "margin-top": "50px"}
                                )),


        ], style={"color": colors['text'], "padding": "5px 5px 5px"}),
    # style={'border': '3px red solid', "color": colors['text'], "padding": "5px 5px 5px"}),


], style={"background-color": "#FAF9F9",
          'margin-right': "3%",
          'margin-left': "3%",
          "box-shadow": "0 3px 10px rgb(0 0 0 / 0.5)",
          'padding': "15px 20px 15px",
          'border-radius': '10px'
          },)


@ app.callback(
    Output(component_id="categorical-variable-distribution-graph",
           component_property='figure'),
    Input(component_id="categorical-variable-distribution-picker",
          component_property='value')
)
def update_categorical_variable_distribution_graph(input_value):
    fig = createPieChartofColumn(input_value)
    return fig


@ app.callback(
    Output(component_id="quantitative-variable-distribution-graph",
           component_property='figure'),
    Input(component_id="quantitative-variable-distribution-picker",
          component_property='value')
)
def update_quantitative_variable_distribution_graph(input_value):
    fig = createHistogramofColumn(input_value)
    return fig


@ app.callback(
    Output(component_id="categorical-variable-distribution-of-promotions-graph",
           component_property='figure'),
    Output(component_id="categorical-variable-distribution-of-promotions-percentages-graph",
           component_property='figure'),
    Input(component_id="categorical-variable-distribution-of-promotions-picker",
          component_property='value')
)
def update_quantitative_variable_distribution_graph(input_value):
    fig1 = plot_promotions_by_cat_variable(input_value)
    fig2 = secure_plot_percentage_promotions_by_cat_variable(input_value, df)
    return fig1, fig2


if __name__ == '__main__':
    app.run_server()
