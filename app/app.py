from flask import Flask, render_template, request, redirect
from plotchart import plotChart, get_EOD_data
from bokeh.embed import components

	
app = Flask(__name__)
#app.config['SECRET_KEY']='secretkey'
app.ticker='QQQ'


@app.route('/', methods=['POST', 'GET'])
def index():
	
	if request.method == 'GET':
		plot = plotChart(app.ticker)
		script, div = components(plot)
		return render_template('index.html',script = script, div = div,title=app.ticker)
#		return render_template('index.html')

	else:
		app.ticker=request.form['ticker']
		plot = plotChart(app.ticker)
		script, div = components(plot)
		return render_template('index.html',script = script, div = div,title=app.ticker)  


if __name__ == '__main__':
	
	app.run(port=33507,debug=True)

