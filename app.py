import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

import findspark
import pyspark


app = dash.Dash()

app.layout = html.Div([
	html.H1('This a basic dashboard'),
	dcc.Graph(
		id = 'basic-graph',
		figure = {
			'data': [go.Scatter(
				x = [1, 2, 3],
				y = [4, 5, 6],
			)],
			'layout': go.Layout(
				title = 'This is our first graph',

			)
		}
	)
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
	app.run_server(debug=True)