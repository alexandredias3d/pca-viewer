import base64
import datetime
import io

import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash.dependencies import Input, Output, State

import pandas as pd

from pathlib import Path
from util import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag-and-Drop or Select Files']),
        multiple=False
    ),
    html.Div(id='parameter-selection')
])

@app.callback(
    Output('parameter-selection', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'),
    prevent_initial_callback=True
)
def update_output(file_content, filename, date):
    if file_content is None:
        return

    if not is_valid_format(filename):
        return html.Div([
            'Invalid file format. pca-viewer only supports .csv files.'
        ])
    
    child = parse_contents(file_content, filename, date)
    return child

def is_valid_format(filename: str) -> bool:
    path = Path(filename)
    format = path.suffix.lower()
    return True if format == '.csv' else False

def parse_contents(contents):
    _, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

    columns = extract_columns(df)

    options = [{'label': column, 'value': index} for index, column in enumerate(columns)]

    return html.Div([
        html.Div([
            html.H5('[Required] Select columns to run PCA on:'),
            dcc.Checklist(
                id='components',
                options=options,
            )],            
            style={'width': '49%', 'display': 'inline-block'}
        ),

        html.Div([
            html.H5('[Optional] Select one column to colorize the data points:'),
            dcc.Dropdown(
                id='color',
                options=options,
            )],
            style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'}
        ),

        html.Hr(),
    ])


if __name__ == '__main__':
    app.run_server(debug=True)