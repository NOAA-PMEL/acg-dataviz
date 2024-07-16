from dash import html, dcc, register_page, callback, Output, Input

# Register the page with Dash
register_page(
    __name__,
    name='Test Page',
    path='/test'
)

# Define the layout for the page
layout = html.Div([
    html.H1("Test Page"),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': 'option1'},
            {'label': 'Option 2', 'value': 'option2'},
            {'label': 'Option 3', 'value': 'option3'}
        ],
        placeholder='Select an option',
        clearable=False
    ),
    html.Div(id='output-div')
])
print("pre-callback")
# Define the callback to update the output based on dropdown selection
@callback(
    Output('output-div', 'children'),
    Input('dropdown', 'value')
)
def update_output(selected_option):
    print("callback triggered")
    if selected_option:
        print("click")
        return f'You selected: {selected_option}'
    return 'Please select an option from the dropdown.'

