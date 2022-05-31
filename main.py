from django.shortcuts import redirect
from flask import Flask, render_template, url_for, redirect
from order_management import order_management

app = Flask(__name__)

@app.route('/')
def index():
    om = order_management()
    context = {
        "pending_positions": om.get_all_pending_orders(),
        "current_positions": om.get_all_current_positions(),
        "pending_close": om.get_all_pending_close_orders(),
        "trade_log": om.get_all_trade_log(),
    }
    om.close_connection()
    return render_template('index.html', context=context)

@app.route('/fill_order/<ticker_one>/<ticker_two>')
def fill_order(ticker_one, ticker_two):
    om = order_management()
    om.fill_order(ticker_one, ticker_two)
    om.close_connection()
    return redirect(url_for('index'))

@app.route('/official_close/<ticker_one>/<ticker_two>')
def official_close(ticker_one, ticker_two):
    om = order_management()
    om.close_position(ticker_one, ticker_two)
    om.close_connection()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)