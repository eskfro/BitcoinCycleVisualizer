import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import yfinance as yf

btc_data = yf.download('BTC-USD', start='2020-01-01', end=datetime.today().strftime('%Y-%m-%d'))
btc_data.reset_index(inplace=True)

plt.style.use('ggplot')
plt.figure(figsize=(10, 5))
plt.plot(btc_data['Date'], btc_data['Close'], label='Close Price', color="tab:blue")
# plt.yscale("log")

today_price = btc_data['Close'].iloc[-1]
today = datetime.today()
date_4yrs_past = today - timedelta(days=4*365 + 1)
past_price = btc_data['Close'].iloc[-365*4]
past_ATH = 67_500
date_biden = datetime(2020, 11, 7)
price_multiplier = past_ATH / past_price

plt.axvline(date_4yrs_past, color='red', linestyle='solid', label='4 Years Ago')
plt.axvline(date_biden, color='green', linestyle='dotted', label='Joe Biden Elected')

plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('BTC-USD')

pady = -5000
plt.text(x=datetime(2021, 10, 10), y=95_000 + pady, s=f"Price Today = {round(today_price)} $")
plt.text(x=datetime(2021, 10, 10), y=90_000 + pady, s=f"Price 4yrs Ago = {round(past_price)} $")
plt.text(x=datetime(2021, 10, 10), y=85_000 + pady, s=f"Past Cycle Multiplier = {round(price_multiplier, 2)}")
plt.text(x=datetime(2021, 10, 10), y=80_000 + pady, s=f"Next ATH (lol) = {round(today_price * price_multiplier)} $")

plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey')
plt.savefig(format = "png", fname="BTC-CycleAnalysis.png")
plt.show()