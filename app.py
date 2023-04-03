from dash import dash 

app = dash.Dash(title='My Board')

print('Bonjour Takam')

app.run_server(debug=True, port=8050)