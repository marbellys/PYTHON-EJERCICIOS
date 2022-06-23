from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='botcoins',vs_currency='usd',days=30)
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp','Price'])