import yfinance as yf
import matplotlib.pyplot as plt

class StockTool:
    def __init__(self):
        pass

    def get_latest_price(self, ticker):
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[-1]
        return price

    def get_historical_data(self, ticker, period='1mo'):
        stock = yf.Ticker(ticker)
        historical_data = stock.history(period=period)
        return historical_data

    def visualize_stock(self, ticker, period='1mo'):
        historical_data = self.get_historical_data(ticker, period)
        plt.figure(figsize=(10, 5))
        plt.plot(historical_data.index, historical_data['Close'], label='Close Price')
        plt.title(f'{ticker} Stock Price Over the Last {period}')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

class StockAgent:
    def __init__(self, tool):
        self.tool = tool

    def perform_task(self, task, ticker, period='1mo'):
        if task == 'get_latest_price':
            price = self.tool.get_latest_price(ticker)
            print(f"The latest price of {ticker} is: ${price:.2f}")
        elif task == 'visualize_stock':
            self.tool.visualize_stock(ticker, period)
        else:
            print("Unknown task.")

if __name__ == "__main__":
    # Creating an instance of the tool and the agent
    stock_tool = StockTool()
    stock_agent = StockAgent(stock_tool)

    # Example usage
    ticker = 'AAPL'  # Apple Inc.
    
    # Getting the latest stock price
    stock_agent.perform_task('get_latest_price', ticker)

    # Visualizing the stock price
    stock_agent.perform_task('visualize_stock', ticker)

