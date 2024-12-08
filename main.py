from price_fetcher import PriceFetcher

# Create an instance of the PriceFetcher class
fetcher = PriceFetcher()

# Connect to Interactive Brokers
fetcher.connect()

# Add some contracts
fetcher.add_contract(contract_type='crypto', symbol='BTC', exchange='PAXOS', currency='USD')
fetcher.add_contract(contract_type='stock', symbol='TLT', exchange='SMART', currency='USD')
fetcher.add_contract(contract_type='forex', symbol='EUR', exchange='', currency='USD')

# Start fetching prices (optional: adjust the interval)
fetcher.start_fetching(interval=1)
