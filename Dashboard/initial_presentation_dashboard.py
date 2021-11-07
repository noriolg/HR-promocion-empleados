import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output
from variables import *
from static_figures import *

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
                style={'border': '3px red solid',
                       "display": "block",
                       "height": "400px"}
            ),

            # 2. Key variables - How are promotions granted?
            # ====================================================
            html.P(dcc.Markdown(children=markdown_part_2_title,
                                style={"text-align": "left",
                                       "color": colors['subtitles'],
                                       "margin-top": "50px"}
                                )),


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


        ], style={'border': '3px red solid', "color": colors['text'], "padding": "5px 5px 5px"}),



], style={"background-color": "#FAF9F9",
          'margin-right': "3%",
          'margin-left': "3%",
          "box-shadow": "0 3px 10px rgb(0 0 0 / 0.5)",
          'padding': "15px 20px 15px",
          'border-radius': '10px'
          },)


@app.callback(
    Output(component_id="my-Div-id",  component_property='children'),
    Input(component_id="my-Input-id", component_property='value')
)
def update_output_div(input_value):
    return "Texto introducido: {0}".format(input_value)


if __name__ == '__main__':
    app.run_server()
