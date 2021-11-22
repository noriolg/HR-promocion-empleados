import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output, State
from variables import *
from plot_functions_part_0 import *
from plot_functions_part_1 import *
from plot_functions_part_2 import *
from predictive_models import *

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
server = app.server


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
                figure=table_initial_variables(),
                id="tabla-inicial",
                style={
                    "display": "block",
                    "height": "400px"}
            ),

            dcc.Graph(
                figure=bar_chart_of_variable_distribution(),
                id="variable-distribution-bar-chart",
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

            html.Div(children=[
                dcc.Markdown(children="Groups with percentages lower than the slider will be grouped into \"Others\" ",
                             style={"text-align": "center",
                                    "color": colors['text'], }
                             ),

                dcc.Slider(id="categorical-variable-distribution-graph-slider", min=0, max=0.1, step=0.01, value=0.05,
                           marks={i: str(int(i*100)) + \
                                  "%" for i in np.linspace(0, 0.1, 11)},
                           )],
                     style={
                "margin-left": "25%",
                "margin-right": "25%",
                "text-align": "center"
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

            dcc.Markdown(children="The distribution of promotions by qualitative variable can be seen in the following pie charts:",
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
                            "display": "inline-block",
                        },
                    ),


                ],
                style={
                    "text-align": "center"
                }
            ),

            dcc.Markdown(children="The distribution of promotions by quantitative variable can be seen in the following pie charts:",
                         style={"text-align": "left",
                                "color": colors['text'], }
                         ),

            html.Div(
                children=[
                    dcc.Dropdown(
                        options=options_quantitative_variables,
                        placeholder="Selecciona una variable",
                        id="quantitative-variable-distribution-of-promotions-picker",
                        style={
                            "display": "block",
                            "width": "300px",
                            "margin-left": "10px"
                        },
                        # Valor por defecto el de la primera variable
                        value=options_quantitative_variables[0]['value']
                    ),


                    html.Div(  # Bloque izquierdo
                        children=[
                               dcc.Graph(
                                   id="quantitative-variable-distribution-of-promotions-percentages-graph",
                                   style={
                                       "display": "block"
                                   }
                               )],
                        style={
                            "width": "700px",
                            "display": "inline-block",
                        },
                    ),

                    html.Div(  # Bloque derecho
                        children=[
                               dcc.Graph(
                                   id="quantitative-variable-distribution-of-promotions-graph",
                                   style={
                                       "display": "block"
                                   }
                               )],
                        style={
                            "width": "700px",
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

            dcc.Graph(
                figure=department_constitution(
                    "Some departments have a higher promotion rate than others, with previous year's ratings being somewhat important"),
                style={
                    "display": "block",
                    "height": "600px"}
            ),

            dcc.Graph(
                figure=department_avg_training_score(
                    "Training scores differ amongst departments and explain promotions adequately"),
                style={
                    "display": "block",
                    "height": "600px"}
            ),

            dcc.Graph(
                figure=avg_training_score_no_of_trainings_promotions(
                    "High training scores almost always get promoted and higher amount of trainings do not matter as much"),
                style={
                    "display": "block",
                    "height": "600px"}
            ),


            dcc.Graph(
                figure=ages_service_lengths(
                    "For every age group, more senior people are more likely to be promoted. In higher age ranges, promotions are more spread out"),
                style={
                    "display": "block",
                    "height": "600px"}
            ),


            # Gender analysis - Is the company an equal opportunity employer?
            dcc.Markdown(children="After arriving to this point and having a better understanding\
                 of the employees and their distribution we wanted to ensure that the business was an equal opportunity employer and that promotions are not biased by gender",
                         style={"text-align": "left",
                                "color": colors['text'], }
                         ),

            dcc.Markdown(children="### The company is an equal opportunity employer",
                         style={"text-align": "center",
                                "color": colors['text'],
                                "margin-top":"70px"}
                         ),

            html.Div(
                children=[

                    html.Div(  # Bloque izquierdo
                        children=[
                               dcc.Graph(
                                   figure=distribution_of_workers_per_department_and_gender_percentages(
                                       "Although male employees represent a higher percentage of workers..."),
                                   style={
                                       "display": "block"
                                   }
                               )],
                        style={
                            "width": "700px",
                            "display": "inline-block",
                        },
                    ),

                    html.Div(  # Bloque derecho
                        children=[
                               dcc.Graph(
                                   figure=distribution_of_workers_per_department_and_gender_absolutes(
                                       "...and they are more prevalent than females in all departments"),
                                   style={
                                       "display": "block"
                                   }
                               )],
                        style={
                            "width": "700px",
                            "display": "inline-block",
                        },
                    ),


                ],
                style={
                    "text-align": "center"
                }
            ),

            html.Div(
                children=[

                    html.Div(  # Bloque izquierdo
                        children=[
                               dcc.Graph(
                                   figure=distribution_of_workers_promotion_per_department_and_gender(
                                       "Percentage of females promoted outshines males in most departments..."),
                                   style={
                                       "display": "block"
                                   }
                               )],
                        style={
                            "width": "700px",
                            "display": "inline-block",
                        },
                    ),

                    html.Div(  # Bloque derecho
                        children=[
                               dcc.Graph(
                                   figure=total_distribution_of_workers_promotion(
                                       "...resulting in a roughly equal promotion percentage"),
                                   style={
                                       "display": "block"
                                   }
                               )],
                        style={
                            "width": "700px",
                            "display": "inline-block",
                        },
                    ),


                ],
                style={
                    "text-align": "center"
                }
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

            html.Div(children=[

                dcc.Markdown(children="### Create an employee profile to predict promotion probability",
                             style={"text-align": "center",
                                    "color": colors['subtitles'],
                                    "margin-top": "50px"}
                             ),

                # Primera línea
                html.Div(children=[

                    # Primera línea, caja izquierda
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Number of trainings:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.Input(
                                    placeholder="Introduce data...",
                                    id="no-of-trainings-picker-for-employee-tool",
                                    type="number",
                                    style={
                                        "width": width_input_components_for_employee_tool,
                                        "margin-left": "15%",
                                        "margin-right": "15%",
                                        "height": "25px"
                                    },
                                ),
                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),
                    ],
                        style={
                            "width": "25%",
                            "display": "inline-block",
                            "margin-left": "5%",
                            "margin-right": "2.5%",
                            "text_align": "center"
                    }
                    ),

                    # Primera línea, caja centro
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Age:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.Input(
                                    placeholder="Introduce data...",
                                    id="age-picker-for-employee-tool",
                                    type="number",
                                    style={
                                        "width": width_input_components_for_employee_tool,
                                        "margin-left": "15%",
                                        "margin-right": "15%",
                                        "height": "25px"
                                    },
                                ),
                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),


                    ],
                        style={
                            "width": "25%",
                            "margin-left": "2.5%",
                            "margin-right": "2.5%",
                            "display": "inline-block"
                    }
                    ),


                    # Primera línea, caja derecha
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Length of service:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.Input(
                                    placeholder="Introduce data...",
                                    id="length-of-service-picker-for-employee-tool",
                                    type="number",
                                    style={
                                        "width": width_input_components_for_employee_tool,
                                        "margin-left": "15%",
                                        "margin-right": "15%",
                                        "height": "25px"
                                    },
                                ),
                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),
                    ],
                        style={
                            "width": "25%",
                            "display": "inline-block",
                            "margin-left": "2.5%",
                            "margin-right": "5%",
                    }
                    ),
                ],
                    style={}
                ),


                # Segunda línea
                html.Div(children=[

                    # Segunda línea, caja izquierda
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Average training score:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.Input(
                                    placeholder="Introduce data...",
                                    id="training-score-picker-for-employee-tool",
                                    type="number",
                                    style={
                                        "width": width_input_components_for_employee_tool,
                                        "margin-left": "15%",
                                        "margin-right": "15%",
                                        "height": "25px",
                                    },
                                ),

                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),


                    ],
                        style={
                            "width": "25%",
                            "display": "inline-block",
                            "vertical-align": "top",
                            "margin-left": "5%",
                            "margin-right": "2.5%",
                    }
                    ),

                    # Segunda línea, caja centro
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Awards won:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.RadioItems(
                                    options=[
                                        {'label': 'I have won awards',
                                            'value': '1'},
                                        {'label': 'I have not won any awards yet',
                                         'value': '0'},
                                    ],
                                    id="award-picker-for-employee-tool",
                                    value='1',
                                    labelStyle={'display': 'flex'},
                                    style={
                                        "margin-left": "40px",
                                    }
                                )
                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),

                    ],
                        style={
                            "width": "25%",
                            "margin-left": "2.5%",
                            "margin-right": "2.5%",
                            "vertical-align": "top",
                            "display": "inline-block"
                    }
                    ),


                    # Segunda línea, caja derecha
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Gender:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.RadioItems(
                                    options=[
                                        {'label': 'Female', 'value': 'f'},
                                        {'label': 'Male',
                                         'value': 'm'},
                                    ],
                                    id="gender-picker-for-employee-tool",
                                    value='f',
                                    labelStyle={'display': 'flex'},
                                    style={
                                        "margin-left": "40px",
                                    }
                                )

                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),


                    ],
                        style={
                            "width": "25%",
                            "display": "inline-block",
                            "vertical-align": "top",
                            "margin-left": "2.5%",
                            "margin-right": "5%",
                    }
                    ),


                ],
                    style={"margin-top": "15px", }),


                # Tercera línea
                html.Div(children=[

                    # Tercera línea, caja izquierda
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Department:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.Dropdown(
                                    options=department_options,
                                    id="department-picker-for-employee-tool",
                                    style={
                                        "display": "block",
                                        "width": "250px",
                                        "margin-left": "20px",
                                    },
                                    # Valor por defecto el de la primera variable
                                    value=department_options[0]['value']
                                ),

                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),


                    ],
                        style={
                            "width": "25%",
                            "display": "inline-block",
                            "margin-left": "5%",
                            "margin-right": "2.5%",
                    }
                    ),

                    # Tercera línea, caja centro
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Education:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.Dropdown(
                                    options=education_options,
                                    id="education-picker-for-employee-tool",
                                    style={
                                        "display": "block",
                                        "width": "250px",
                                        "margin-left": "20px",
                                    },
                                    # Valor por defecto el de la primera variable
                                    value=education_options[0]['value']
                                ),
                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),
                    ],
                        style={
                            "width": "25%",
                            "margin-left": "2.5%",
                            "margin-right": "2.5%",
                            "display": "inline-block"
                    }
                    ),


                    # Tercera línea, caja derecha
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Recruitment channel:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.Dropdown(
                                    options=recruitment_options,
                                    id="recruitment-picker-for-employee-tool",
                                    style={
                                        "display": "block",
                                        "width": "250px",
                                        "margin-left": "20px",
                                    },
                                    # Valor por defecto el de la primera variable
                                    value=recruitment_options[0]['value']
                                ),

                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%",
                            },
                        ),
                    ],
                        style={
                            "width": "25%",
                            "display": "inline-block",
                            "margin-left": "2.5%",
                            "margin-right": "5%"
                    }
                    ),
                ],
                    style={"margin-top": "15px", }
                ),


                # Cuarta línea
                html.Div(children=[

                    # Cuarta línea, caja izquierda
                    html.Div(children=[

                        html.Div(
                            children=[
                                dcc.Markdown(children="Previous year rating:",
                                             style={"text-align": "left",
                                                    "color": colors['text'],
                                                    "margin-top": "25px"}
                                             ),

                                dcc.Slider(
                                    id='previous-year-rating-picker-for-employee-tool',
                                    min=0,
                                    max=5,
                                    step=1,
                                    value=3,
                                    marks={0: '0', 1: '1', 2: '2',
                                           3: '3', 4: '4', 5: '5'},
                                ),
                            ],
                            style={
                                "display": "block",
                                "width": width_div_components_for_employee_tool,
                                "margin-left": "10%",
                                "margin-right": "10%"
                            },
                        ),
                    ],
                        style={
                            "width": "25%",
                            "display": "inline-block",
                            "margin-left": "5%",
                            "margin-right": "2.5%"}
                    ),

                    # Cuarta línea, caja centro
                    html.Div(children=[


                        html.Button('Generate Profile', id='submit-button', n_clicks=0,
                                    style={"width": "250px",
                                           "height": "40px",
                                           "font-weight": "bold",
                                           "background-color": '#E1ECF7',
                                           "font-size": "18px",
                                           "border-radius": "100px"})

                    ],
                        style={
                            "width": "25%",
                            "margin-left": "2.5%",
                            "margin-right": "2.5%",
                            "margin-top": "40px",
                            "vertical-align": "top",
                            "display": "inline-block",
                            "text-align": "center"}
                    ),


                    # Cuarta línea, caja derecha
                    html.Div(children=[

                        dcc.Markdown(children=" ",
                                     style={"text-align": "right",
                                            "color": colors['text'],
                                            "margin-top": "25px"}
                                     ),

                    ],
                        style={
                            "width": "25%",
                            "text-align": "center",
                            "display": "inline-block",
                            "margin-left": "2.5%",
                            "margin-right": "5%",
                    }
                    ),


                ],
                    style={"margin-top": "15px"}
                ),



                dcc.Markdown(id="employee-profile-message",
                             style={"text-align": "center",
                                    "color": colors['text'],
                                    "border-radius":"10px",
                                    "background-color": "#FBFAFA",
                                    "width": "70%",
                                    "padding": "5px 5px 5px 5px",
                                    "margin-left": "15%",
                                    "margin-top": "25px"}
                             ),

            ],
                style={"background-color": "#F3F3F3",
                       'margin-right': "3%",
                       'margin-left': "3%",
                       "box-shadow": "0 3px 10px rgb(0 0 0 / 0.5)",
                       'padding': "15px 20px 15px",
                       'border-radius': '10px',
                       }
            ),




            html.Div(children=[


                html.Div([
                    dcc.Tabs(id="tabs", value='tab-1', children=[
                        dcc.Tab(label='Promotion probability', value='tab-1'),
                        dcc.Tab(label='Employee comparison', value='tab-2'),
                    ]),
                    html.Div(id='tabs-content')
                ]),

            ],
                style={"background-color": "#F3F3F3",
                       'margin-top': "10px",
                       'margin-right': "3%",
                       'margin-left': "3%",
                       "box-shadow": "0 3px 10px rgb(0 0 0 / 0.5)",
                       'padding': "15px 20px 15px",
                       'border-radius': '10px'
                       }
            )



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
          component_property='value'),
    Input(component_id="categorical-variable-distribution-graph-slider",
          component_property='value')

)
def update_categorical_variable_distribution_graph(input_value, slider_input):
    fig = createPieChartofColumn(input_value, slider_input)
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
def update_qualitative_variable_promotion_distribution_graph(input_value):
    fig1 = plot_promotions_by_cat_variable(input_value)
    fig2 = plot_percentage_promotions_by_cat_variable(input_value)
    return fig1, fig2


@ app.callback(
    Output(component_id="quantitative-variable-distribution-of-promotions-graph",
           component_property='figure'),
    Output(component_id="quantitative-variable-distribution-of-promotions-percentages-graph",
           component_property='figure'),
    Input(component_id="quantitative-variable-distribution-of-promotions-picker",
          component_property='value')
)
def update_quantitative_variable_promotion_distribution_graph(input_value):
    fig1 = plot_promotions_by_quant_variable(input_value)
    fig2 = plot_percentage_promotions_by_quant_variable(input_value)
    return fig1, fig2


@ app.callback(
    Output(component_id="employee-profile-message",
           component_property='children'),
    Output(component_id="submit-button",
           component_property='n_clicks'),
    Output(component_id="model-output-div",
           component_property='children'),
    Input(component_id="submit-button",
          component_property="n_clicks"),
    State(component_id="no-of-trainings-picker-for-employee-tool",
          component_property='value'),
    State(component_id="age-picker-for-employee-tool",
          component_property='value'),
    State(component_id="length-of-service-picker-for-employee-tool",
          component_property='value'),
    State(component_id="training-score-picker-for-employee-tool",
          component_property='value'),
    State(component_id="award-picker-for-employee-tool",
          component_property='value'),
    State(component_id="gender-picker-for-employee-tool",
          component_property='value'),
    State(component_id="department-picker-for-employee-tool",
          component_property='value'),
    State(component_id="education-picker-for-employee-tool",
          component_property='value'),
    State(component_id="recruitment-picker-for-employee-tool",
          component_property='value'),
    State(component_id="previous-year-rating-picker-for-employee-tool",
          component_property='value'),
)
def register_data_from_employee_profile_and_run_predicion_model(submit_button_value, no_of_trainings, age, length_of_service, training_score, award, gender, department, education, recruitment, previous_year_rating):

    # Esta función genera el texto a mostrar al usuario y nos indica si ha de correrse el modelo de predicción o no
    user_text, modelo_ok = generate_user_text(submit_button_value, no_of_trainings, age, length_of_service,
                                              training_score, award, gender, department, education, recruitment, previous_year_rating)

    # Sumamos uno al submit_button_value para saber que ya no es la primer vez que está en pantalla
    submit_button_value = submit_button_value + 1

    # En caso de que el modelo esté ok, se hace la predicción
    if modelo_ok:
        prediction_text = generate_promotion_prediction(no_of_trainings, age, length_of_service,
                                                        training_score, award, gender, department, education, recruitment, previous_year_rating)

    else:
        prediction_text = "No hay nada"
        # En caso de que no se corra la predicción del modelo, únicamente devolvemos dos cosas

    return user_text, submit_button_value, prediction_text


@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':

        return html.Div(
            [
                html.H3('Tab content 1'),
                dcc.Markdown(children="Aquí irá el modelo",
                             style={"text-align": "left",
                                    "color": colors['text'],
                                    "margin-top": "25px"}
                             ),
                html.Div(
                    id='model-output-div', children=["Aquí ya no hay nada de nada"], style={'border': '2px blue solid'}),
            ]
        )
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Markdown(children="Aquí irá la comparación del empleado con el resto de panas",
                         style={"text-align": "left",
                                "color": colors['text'],
                                "margin-top": "25px"}
                         ),

        ])


if __name__ == '__main__':
    app.run_server()
