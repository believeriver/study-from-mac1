from dash import Dash, html, Output, Input, State, dcc, ctx
import dash_bootstrap_components as dbc

ROW_BORDER = {
    # 'border-color': 'red',      # border-color: red
    # 'border-style': 'solid',    # border-style: dotted, solid, double   
    # 'border-width': 'thin',     # border-width: thin, thick
    # 'text-align': 'center'
}

COL_BORDER = {
    'border-color': 'green',    # border-color: green
    'border-style': 'dotted',   # border-style: dotted, solid, double   
    'border-width': 'thin',     # border-width: thin, thick
    'text-align': 'center',
}

######################
def get_row() -> list:
    return [dbc.Col(html.Div(f"col{i}"), style=COL_BORDER) for i in range(1,13)]                         

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) 

### Row with columns

layout_row = get_row()

app.layout = dbc.Container(
    [
        # Layout Template Row
        dbc.Row(layout_row),
        dbc.Row(html.Br()),

        # Row1
        dbc.Row(
            # Row1, Col1
            dbc.Col(html.Div("row1, col1"), style=COL_BORDER), 
            style=ROW_BORDER
        ),
        dbc.Row(html.Br()),

        # Row2
        dbc.Row(
            [
                # Row2, Col1        
                dbc.Col(html.Div("row2, col1"), style=COL_BORDER),
                # Row2, Col2
                dbc.Col(html.Div("row2, col2"), style=COL_BORDER),
            ],
            style=ROW_BORDER,    
        ),
        dbc.Row(html.Br()),        

        # Row3
        dbc.Row(
            [
                # Row3, Col1        
                dbc.Col(html.Div("row3, col1"), style=COL_BORDER),
                # Row3, Col2
                dbc.Col(html.Div("row3, col2"), style=COL_BORDER),
                # Row3, Col3
                dbc.Col(html.Div("row3, col3"), style=COL_BORDER),
            ],
            style=ROW_BORDER,    
        ),        
    ], fluid=False,
)    

if __name__ == '__main__':
    app.run_server(debug=True)  