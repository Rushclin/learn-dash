from dash import dash 
import d

app = dash.Dash(title='My Board')

print('Bonjour Takam')

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)