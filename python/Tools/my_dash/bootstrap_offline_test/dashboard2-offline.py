import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

# app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])
app=dash.Dash()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

sidebar = html.Div(
    [
        dbc.Row(
            [
                html.P('Sidebar')
            ],
            style={"height": "5vh"}, className='bg-primary text-white'
        ),
        dbc.Row(
            [
                html.P('Categorical and Continuous Variables')
            ],
            style={"height": "50vh"}, className='bg-secondary text-white'
        ),
        dbc.Row(
            [
                html.P('Target Variables')
            ],
            style={"height": "45vh"}, className='bg-dark text-white'
        )
    ]
)
content = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('Distribution of Categorical Variable'),
                    ],
                    # className='bg-white'
                ),
                dbc.Col(
                    [
                        html.P('Distribution of Continuous Variable')
                    ],
                    # className='bg-dark text-white'
                )
            ],
            style={"height": "50vh"}
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.P('Correlation Matrix Heatmap')
                    ],
                    # className='bg-light'
                )
            ],
            style={"height": "50vh"}
        )
    ]
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=3, className='bg-light'),
                dbc.Col(content, width=9)
            ],
            style={"height": "100vh"}
        ),
    ],
    fluid=True
)


if __name__ == '__main__':
    app.run_server(debug=True, port=1234)