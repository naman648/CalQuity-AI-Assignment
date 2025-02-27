## 📜 Instructions to Replicate the Output

### STEP 1️⃣: Set Up Your Environment

- Install Python: Ensure you have Python installed on your machine. You can download it from python.org.

- Install Required Libraries: Open a terminal or command prompt and install the required libraries using pip. Run the following commands:
```sh
pip install yfinance matplotlib
```
### STEP 2️⃣: Create the Python Script

- Create a New File: Open your preferred text editor or IDE (such as VSCode, PyCharm, or even Notepad) and create a new file named stock_analysis.py.

### STEP 3️⃣: Copy the Code

- Copy the following code into the stock_analysis.py file:
```sh
import yfinance as yf
import matplotlib.pyplot as plt

class StockTool:
    def __init__(self):
        pass

    def get_latest_price(self, ticker):
        """Fetch the latest stock price for the given ticker."""
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[-1]
        return price

    def get_historical_data(self, ticker, period='1mo'):
        """Fetch historical stock data for the given ticker and period."""
        stock = yf.Ticker(ticker)
        historical_data = stock.history(period=period)
        return historical_data

    def visualize_stock(self, ticker, period='1mo'):
        """Visualize the historical stock prices for the given ticker."""
        historical_data = self.get_historical_data(ticker, period)
        plt.figure(figsize=(10, 5))
        plt.plot(historical_data.index, historical_data['Close'], label='Close Price', color='blue')
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
        """Perform a specified task using the stock tool."""
        if task == 'get_latest_price':
            price = self.tool.get_latest_price(ticker)
            print(f"The latest price of {ticker} is: ${price:.2f}")
        elif task == 'visualize_stock':
            self.tool.visualize_stock(ticker, period)
        else:
            print("Unknown task.")

if __name__ == "__main__":
    # Create an instance of the tool and the agent
    stock_tool = StockTool()
    stock_agent = StockAgent(stock_tool)

    # Example usage
    ticker = 'AAPL'  # Apple Inc.
    
    # Get the latest stock price
    stock_agent.perform_task('get_latest_price', ticker)

    # Visualize the stock price
    stock_agent.perform_task('visualize_stock', ticker)
```
### STEP 4️⃣: Run the script

- Open a Terminal or Command Prompt: Navigate to the directory where you saved the stock_analysis.py file.

- Execute the script by running the following command:
```sh
python stock_analysis.py
```
### STEP 5️⃣: Observe the Output

- Latest Stock Price: The script will print the latest stock price for Apple Inc. (AAPL) in the terminal or command prompt.

- Stock Price Visualization: A plot will be displayed showing the historical closing prices for AAPL over the last month.

### STEP 6️⃣: Customization

- Change the Ticker: You can modify the ticker variable in the __main__ section to fetch data for different stocks. For example, change ticker = 'AAPL' to ticker = 'GOOGL' for Google.

- Change the Period: You can also modify the period parameter in the perform_task method calls to visualize different time frames (e.g., '1w', '3mo', '1y').

