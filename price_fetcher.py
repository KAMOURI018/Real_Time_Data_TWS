from ib_insync import IB, Stock, Forex, Crypto
import time

class PriceFetcher:
    def __init__(self, host='127.0.0.1', port=7497, client_id=1):
        self.ib = IB()
        self.host = host
        self.port = port
        self.client_id = client_id
        self.contracts = []

    def connect(self):
        self.ib.connect(self.host, self.port, clientId=self.client_id)
        print("Connected to Interactive Brokers.")

    def add_contract(self, contract_type, symbol, exchange, currency):
        if contract_type == 'crypto':
            contract = Crypto(symbol, exchange, currency)
        elif contract_type == 'stock':
            contract = Stock(symbol, exchange, currency)
        elif contract_type == 'forex':
            contract = Forex(symbol + currency)
        else:
            raise ValueError("Unsupported contract type. Use 'crypto', 'stock', or 'forex'.")

        # Qualify the contract and check for errors
        qualified_contract = self.ib.qualifyContracts(contract)
        if not qualified_contract:
            print(f"Error qualifying contract: {contract}")
        else:
            self.contracts.append(contract)
            print(f"Added and qualified contract: {qualified_contract[0]}")

    def fetch_prices(self):
        if not self.contracts:
            print("No contracts added. Please add a contract first.")
            return

        for contract in self.contracts:
            try:
                data = self.ib.reqMktData(contract)

                # Allow some time for data to update
                self.ib.sleep(0.5)

                # Print the real-time market data
                print(f"Real-time market data for {contract.localSymbol}:")
                print(f"Last price: {data.last}, Bid: {data.bid}, Ask: {data.ask}")
                print("-" * 50)
            except Exception as e:
                print(f"Error fetching data for {contract.localSymbol}: {e}")

    def start_fetching(self, interval=1):
        try:
            print("Starting to fetch prices. Press Ctrl+C to stop.")
            while True:
                self.fetch_prices()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Stopped fetching prices.")
        finally:
            self.disconnect()

    def disconnect(self):
        self.ib.disconnect()
        print("Disconnected from Interactive Brokers.")

# Example usage:
if __name__ == "__main__":
    fetcher = PriceFetcher()
    fetcher.connect()

    # Add contracts with debugging output
    fetcher.add_contract(contract_type='crypto', symbol='BTC', exchange='PAXOS', currency='USD')
    fetcher.add_contract(contract_type='stock', symbol='AAPL', exchange='SMART', currency='USD')
    fetcher.add_contract(contract_type='forex', symbol='EUR', exchange='', currency='USD')

    # Start fetching data
    fetcher.start_fetching(interval=1)
