"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, ctx, html
import plotly.express as px
import plotly.graph_objects as go

import pandas as pd
import os
import datetime

import graph_views

#get date
dt_now = datetime.datetime.now()
print(dt_now.year, dt_now.month, dt_now.day)
print(type(dt_now.year))

# set select items
area_list = ['ライセンス','長崎流体機','高砂流体機','神戸流体機']
items_license = ['NASTRAN','Abaqus','Fluent','CFX']
items_nagasaki = ['Sandybridge','Ivybridge', 'Ivybridge2', 'Haswell', 'Broadwell', 'Skylake']
items_takasago = ['R5_Ivybridge', 'R5_Haswell2', 'R5_Broadwell', 'R5_Broadwell2', 'R5_Skylake']
items_kobe = ['Cascadelake', 'Milan']

year_list =[item for item in range(2020, dt_now.year+1)]
year_list.append('-')
month_list = [item for item in range(1,13)]
month_list.append('-')
# for item in year_list:
#     print(item)
# for item in month_list:
#     print(item)

#import datasets
datasets = graph_views.fetch_dataset(dt_now.year, dt_now.month)
#initial graph
figure_datasets = graph_views.create_figure(datasets, items_license, area_list[0])
fig1 = figure_datasets.create_figure(0,100)
figure_datasets = graph_views.create_figure(datasets, items_nagasaki, area_list[1])
fig2 = figure_datasets.create_figure(0,100)
figure_datasets = graph_views.create_figure(datasets, items_takasago, area_list[2])
fig3 = figure_datasets.create_figure(0,100)
figure_datasets = graph_views.create_figure(datasets, items_kobe ,area_list[3])
fig4 = figure_datasets.create_figure(0,100)

del datasets,figure_datasets

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    # "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    # "width": "20rem",
    "padding": "2rem 1rem",
    # "color":"#fff",
    # "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H4("Settings", className="display-7"),
        html.Hr(),
        # html.P(
        #     "Please select license or area", className="lead"
        # ),
        # html.Label('最新の24時間のみ表示する'),
        dcc.Checklist(
            options=[{'label':'最新の1日のみ表示する', 'value': 'True'}],
            id='selected-24-hours', className="text-warning"),
        html.Hr(),
        html.Label('年'),
        html.Div([
            dcc.Dropdown(
                year_list,
                dt_now.year,
                id='year-select'
            ),
        ], style={'width': '98%', 'display': 'inline-block'}),
        # html.Hr(),
        html.Label('月'),
        html.Div([
            dcc.Dropdown(
                month_list,
                dt_now.month,
                id='month-select',
            ),
        ], style={'width': '98%', 'display': 'inline-block'}),
        html.Hr(),
        html.Label('ライセンス'),
        dcc.Dropdown(items_license,
                     items_license,
                     id='selected-license',
                     multi=True),
        html.Label('長崎流体機'),
        dcc.Dropdown(items_nagasaki,
                     items_nagasaki,
                     id='selected-nagasaki',
                     multi=True),
        html.Label('高砂流体機'),
        dcc.Dropdown(items_takasago,
                     items_takasago,
                     id='selected-takasago',
                     multi=True),
        html.Label('神戸流体機'),
        dcc.Dropdown(items_kobe,
                     items_kobe,
                     id='selected-kobe',
                     multi=True),
        html.Hr(),
        # dbc.Button("Draw Graph", id='draw', color="primary", className="me-1"),
        # dbc.Button("Rest Graph", id='reset', color="success", className="me-1"),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div([
    html.H6("Availability status of trend data."),
    dcc.Graph(id='graph_1',figure=fig1),
    dcc.Graph(id='graph_2',figure=fig2),
    dcc.Graph(id='graph_3',figure=fig3),
    dcc.Graph(id='graph_4',figure=fig4),
])
# app.layout = dbc.Container(
app.layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=4, className='bg-secondary'),
                dbc.Col(content, width=8, className='bg-white')
            ]
        )
    ]
)
@app.callback(
    Output(component_id='graph_1', component_property='figure'),
    # Input('draw', 'n_clicks'),
    # State('selected-license','value'),
    Input('selected-24-hours','value'),
    Input('selected-license','value'),
    Input('year-select','value'),
    Input('month-select','value'),
    prevent_initial_call=True
)
# def update_graph(draw,items,year,month):
def update_graph(flg,items,year,month):
    # print(flg)
    # triggered_id = ctx.triggered_id
    # print(items)
    # if triggered_id == 'draw':
    #     print('*** draw ***')
    #     return draw_graph(items, year, month)
    return draw_graph(flg,items, year, month)
def draw_graph(flg,items, year, month):
    datasets = graph_views.fetch_dataset(year, month)
    figure_datasets = graph_views.create_figure(datasets, items ,'ライセンス', flg)
    fig1 = figure_datasets.create_figure(0,100)
    del datasets,figure_datasets
    return fig1
def reset_graph():
    return go.Figure()

@app.callback(
    Output(component_id='graph_2', component_property='figure'),
    Input('selected-24-hours','value'),
    Input('selected-nagasaki','value'),
    Input('year-select','value'),
    Input('month-select','value'),
    prevent_initial_call=True
)
def update_graph2(flg,items,year,month):
    return draw_graph2(flg,items, year, month)
def draw_graph2(flg, items, year, month):
    datasets = graph_views.fetch_dataset(year, month)
    figure_datasets = graph_views.create_figure(datasets, items, '長崎流体機', flg)
    fig2 = figure_datasets.create_figure(0,100)
    del datasets,figure_datasets
    return fig2

@app.callback(
    Output(component_id='graph_3', component_property='figure'),
    Input('selected-24-hours','value'),
    Input('selected-takasago','value'),
    Input('year-select','value'),
    Input('month-select','value'),
    prevent_initial_call=True
)
def update_graph3(flg,items,year,month):
    return draw_graph3(flg,items, year, month)
def draw_graph3(flg,items, year, month):
    datasets = graph_views.fetch_dataset(year, month)
    figure_datasets = graph_views.create_figure(datasets, items, '高砂流体機', flg)
    fig3 = figure_datasets.create_figure(0,100)
    del datasets,figure_datasets
    return fig3

@app.callback(
    Output(component_id='graph_4', component_property='figure'),
    Input('selected-24-hours','value'),
    Input('selected-kobe','value'),
    Input('year-select','value'),
    Input('month-select','value'),
    prevent_initial_call=True
)
def update_graph4(flg,items,year,month):
    return draw_graph4(flg,items, year, month)
def draw_graph4(flg, items, year, month):
    datasets = graph_views.fetch_dataset(year, month)
    figure_datasets = graph_views.create_figure(datasets, items, '神戸流体機', flg)
    fig4 = figure_datasets.create_figure(0,100)
    del datasets,figure_datasets
    return fig4

if __name__ == "__main__":
    app.run_server(port=8000)