# Price Fetcher

**Price Fetcher** is a Python-based application that connects to Interactive Brokers (IB) to fetch real-time market data for crypto, stocks, and forex. It enables users to manage contracts and retrieve prices with ease.

---

## Features

- **Connect to IB Gateway**: Establishes a connection to the Interactive Brokers system.
- **Add Contracts**: Supports adding crypto, stocks, and forex contracts.
- **Fetch Real-time Prices**: Retrieves last price, bid, and ask prices for added contracts.
- **Continuous Fetching**: Periodically fetches price data at user-defined intervals.
- **Error Handling**: Provides error messages for contract qualification and data retrieval.

---

## Prerequisites

- **Interactive Brokers Gateway or TWS** installed and running.
- Python 3.8+
- Required Python packages:
  - `ib_insync`

Install dependencies:

```bash
pip install ib_insync
```

---

## Usage

### Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Ensure the IB Gateway or TWS is running and accessible.

### Running the Application

1. Run the script:
   ```bash
   python price_fetcher.py
   ```
2. Example usage:
   - Adds contracts (crypto, stock, forex):
     ```python
     fetcher.add_contract(contract_type='crypto', symbol='BTC', exchange='PAXOS', currency='USD')
     fetcher.add_contract(contract_type='stock', symbol='AAPL', exchange='SMART', currency='USD')
     fetcher.add_contract(contract_type='forex', symbol='EUR', exchange='', currency='USD')
     ```
   - Fetch real-time market prices periodically:
     ```python
     fetcher.start_fetching(interval=1)
     ```

### Stopping the Application

- Use `Ctrl+C` to stop continuous fetching.

---

## Class and Method Details

### **PriceFetcher**

#### **Methods:**

- `__init__(host, port, client_id)`: Initialize connection details.
- `connect()`: Connect to Interactive Brokers.
- `add_contract(contract_type, symbol, exchange, currency)`: Add and qualify contracts.
- `fetch_prices()`: Fetch and print market data for added contracts.
- `start_fetching(interval)`: Continuously fetch prices at a specified interval.
- `disconnect()`: Disconnect from Interactive Brokers.

---

## Example Output

Example real-time market data:

```
Real-time market data for BTCUSD:
Last price: 50000, Bid: 49980, Ask: 50020
--------------------------------------------------
Real-time market data for AAPL:
Last price: 150, Bid: 149.5, Ask: 150.5
--------------------------------------------------
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add a feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Support

For issues, please open an [issue](https://github.com/your-repo-url/issues) on GitHub or contact the repository owner.
