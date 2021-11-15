import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output


app = dash.Dash()

markdown_title = "## This is a markdown title"

markdown_text = """
We can use markdown to escribir cosas muy bien y que queden muy bonitas. Por ejemplo las conclusiones del proyecto

* Esto es una lista
* Segundo elemento
* Introduce un elemento en la caja de texto aquí debajo
"""

# Creating Data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([
    "This is the outermost Div",

    html.Div(
        ['This is an inner div!'],
        style={'color': 'red', 'border': '3px red solid'}
    ),


    html.P(html.Label('Dropdown')),

    dcc.Dropdown(options=[{'label': 'Test label 1',
                           'value': 'test_lab_1'},
                          {'label': 'Test label 2',
                           'value': 'test_lab_2'}
                          ],
                 value="test_lab_1"
                 ),

    dcc.Markdown(children=markdown_title,
                 style={"text-align": "center"}
                 ),


    dcc.Markdown(children=markdown_text,
                 ),

    dcc.Input(id='my-Input-id', value="Initial text value", type="text"),
    html.Div(id='my-Div-id', style={'border': '2px blue solid'}),

    html.P(html.Label('Slider')),
    dcc.Slider(min=-10, max=10, step=0.5, value=0,
               marks={i: i for i in range(-10, 11)}),

    html.P(html.Label('Radio items')),
    dcc.RadioItems(options=[{'label': 'Test label 1',
                             'value': 'test_lab_1'},
                            {'label': 'Test label 2',
                             'value': 'test_lab_2'}
                            ],
                   value="test_lab_1"),

    dcc.Graph(id='scatterplot_basic',
              figure={"data": [
                  go.Scatter(
                      x=random_x,
                      y=random_y,
                      mode='markers',
                      marker={
                          'size': 12,
                          'color': "salmon",
                          "symbol": "pentagon",
                          "line": {"width": 2}
                      }
                  )],
                  "layout": go.Layout(title="My Scatterplot",
                                      xaxis={"title": "Some X title"})}
              ),

    html.Div(
        ['Another inner div'],
        style={'color': 'blue', 'border': '3px blue solid'}
    ),

    dcc.Graph(id='scatterplot_basic_2',
              figure={"data": [
                  go.Scatter(
                      x=random_x,
                      y=random_y,
                      mode='markers',
                      marker={
                          'size': 11,
                          'color': "blue",
                          "symbol": "circle",
                          "line": {"width": 3}
                      }
                  )],
                  "layout": go.Layout(title="My Scatterplot",
                                      xaxis={"title": "Another X title"})}
              )
], style={'border': '2px green solid'})


@app.callback(
    Output(component_id="my-Div-id",  component_property='children'),
    Input(component_id="my-Input-id", component_property='value')
)
def update_output_div(input_value):

    return "Texto introducido: {0}".format(input_value)


if __name__ == '__main__':
    app.run_server()
