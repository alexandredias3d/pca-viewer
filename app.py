import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from pca_helper import *
from util import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

button_style = {
    'width': '99%',
    'height': '60px',
    'lineHeight': '60px',
    'borderWidth': '1px',
    'borderStyle': 'solid',
    'borderRadius': '5px',
    'textAlign': 'center',
    'margin': '10px'
}

app.layout = html.Div([
    html.Div(
        dcc.Upload(
            id='upload-data',
            children=html.Button('Select .csv file', style=button_style),
            multiple=False,
        ),
        id='upload'
    ),
    html.Hr(),
    html.Div(
        html.Div([
            html.Div([
                html.H5('[Required] Select columns to run PCA on:'),
                dcc.Checklist(
                    id='components',
                    options=[{'label': '', 'value' : ''}],
                )],            
                style={'width': '49%', 'display': 'inline-block'}
            ),
            html.Div([
                html.H5('[Optional] Select one column to colorize the data points:'),
                dcc.Dropdown(
                    id='color',
                    options=[{'label': '', 'value' : ''}],
                )],
                style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'}
            ),
        ]),
        id='parameter-selection'),
    html.Hr(),
    html.Div(
        html.Button
        (
            'Run PCA', 
            id='run-pca', 
            n_clicks=0, 
            style=button_style,
        ),
        id='run'
    ),
    html.Hr(),
    html.Div(
        id='pca-results',
        children=
        [
            html.H5('PCA Results'),
            dcc.Graph(id='pca-chart', style={'width': '100%', 'height': '100vh'}),
        ]
    )
])

@app.callback(
    [Output('components', 'options'), Output('color', 'options')],
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    prevent_initial_call=True
)
def update_output(file_content, filename):
    if file_content is None:
        return

    if not is_valid_format(filename):
        return html.Div([
            'Invalid file format. pca-viewer only supports .csv files.'
        ])
    
    df = parse_contents(file_content)
    columns = extract_columns(df)
    options = [{'label': column, 'value': index} for index, column in enumerate(columns)]

    return options, options

@app.callback(
    Output('pca-chart', 'figure'),
    Input('run-pca', 'n_clicks'),
    State('upload-data', 'contents'),
    State('components', 'value'),
    State('color', 'value'),
    prevent_initial_call=True
)
def run_pca_on_click(button_click, contents, components, selected_color):

    if not components:
        raise PreventUpdate

    if contents is None:
        return {}

    csv = decode(contents)
    data = read_csv(csv)

    columns = extract_columns(data)

    feature_dimensions = columns[components]
    features = select_columns(data, feature_dimensions)

    if has_color(selected_color):
        color_dimension = columns[selected_color]
        color = select_columns(data, color_dimension)
    else:
        color = None

    normalized = normalize_data(features)
    reduced = run_pca(normalized)

    fig = plot(reduced, color)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)