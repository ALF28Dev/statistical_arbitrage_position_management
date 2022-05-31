import sqlite3

class ticker():
    def __init__(self, ticker, price, size):
        self.ticker = ticker
        self.price = price
        self.size = size

''' Manage the orders database '''
class order_management():
    def __init__(self):
        self.connection = sqlite3.connect('order_database.db')
        self.cursor = self.connection.cursor()
    
    ''' Create a new pending order. '''
    def new_pending_order(self, ticker_one, ticker_two):
        parameters = (ticker_one.ticker, ticker_one.price, ticker_one.size, ticker_two.ticker, ticker_two.price, ticker_two.size)
        self.cursor.execute("insert into pending_orders values (?, ?, ?, ?, ?, ?)", parameters)
        self.connection.commit()

    ''' Create a new filled order and remove it from the pending order table. '''
    def fill_order(self, ticker_one, ticker_two):
        self.cursor.execute("SELECT * FROM pending_orders WHERE buy_ticker=? and sell_ticker=?", (ticker_one, ticker_two,))
        data = self.cursor.fetchone()
        stock_one = ticker(data[0], data[1], data[2])
        stock_two = ticker(data[3], data[4], data[5])
        parameters = (stock_one.ticker, stock_one.price, stock_one.size, stock_two.ticker, stock_two.price, stock_two.size)
        self.cursor.execute("insert into filled_orders values (?, ?, ?, ?, ?, ?)", parameters)
        self.cursor.execute("DELETE FROM pending_orders WHERE buy_ticker=? and sell_ticker=?", (ticker_one,ticker_two,))
        self.connection.commit()

    ''' Create a new pending close order with the latest prices for both stocks within the pair. '''
    def new_pending_close(self, ticker_one, ticker_one_price,ticker_two, ticker_two_price):
        self.cursor.execute("SELECT * FROM filled_orders WHERE buy_ticker=? and sell_ticker=?", (ticker_one, ticker_two,))
        data = self.cursor.fetchone()
        stock_one = ticker(data[0], ticker_one_price, data[2])
        stock_two = ticker(data[3], ticker_two_price, data[5])
        parameters = (stock_one.ticker, stock_one.price, stock_one.size, stock_two.ticker, stock_two.price, stock_two.size)
        self.cursor.execute("insert into pending_close values (?, ?, ?, ?, ?, ?)", parameters)
        self.connection.commit()

    ''' Close a position and place it within the trade_logs table. Remove it from the pending_close and filled_orders tables. '''
    def close_position(self, ticker_one, ticker_two):
        print("here")
        self.cursor.execute("SELECT * FROM pending_close WHERE buy_ticker=? and sell_ticker=?", (ticker_one, ticker_two,))
        pending_close_data = self.cursor.fetchone()
        self.cursor.execute("SELECT * FROM filled_orders WHERE buy_ticker=? and sell_ticker=?", (ticker_one, ticker_two,))
        filled_orders_data = self.cursor.fetchone()
        ticker_one_pl = pending_close_data[1]-filled_orders_data[1]
        ticker_two_pl = filled_orders_data[4]-pending_close_data[4]
        parameters = (ticker_one, ticker_one_pl, ticker_two, ticker_two_pl, ticker_one_pl+ticker_two_pl)
        self.cursor.execute("insert into trade_log values (?, ?, ?, ?, ?)", parameters)
        self.cursor.execute("DELETE FROM filled_orders WHERE buy_ticker=? and sell_ticker=?", (ticker_one,ticker_two,))
        self.cursor.execute("DELETE FROM pending_close WHERE buy_ticker=? and sell_ticker=?", (ticker_one,ticker_two,))
        self.connection.commit()

    def get_all_pending_close_orders(self):
        self.cursor.execute("SELECT * FROM pending_close")
        return self.cursor.fetchall()

    def get_all_trade_log(self):
        self.cursor.execute("SELECT * FROM trade_log")
        return self.cursor.fetchall()

    def get_all_pending_orders(self):
        self.cursor.execute("SELECT * FROM pending_orders")
        return self.cursor.fetchall()

    def get_all_current_positions(self):
        self.cursor.execute("SELECT * FROM filled_orders")
        return self.cursor.fetchall()

    ''' Check if a trade is currently open for a specific pair '''
    def check_for_open_position(self, ticker_one, ticker_two):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM filled_orders WHERE buy_ticker=? and sell_ticker=?", (ticker_one, ticker_two,))
        return cursor.fetchone()

    def close_connection(self):
        self.connection.close()
