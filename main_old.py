import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('DeriBit_BTC_PERPETUAL_d.csv', skiprows=1)

# Parse the date column
df['date'] = pd.to_datetime(df['date'])

today = datetime.today()
four_year_before_today = today - timedelta(days= 4*365 + 1)
biden_elected_president = datetime(2020, 11, 7)

# Plot the date and close prices
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['close'], label='Close Price')

plt.axvline(four_year_before_today, color='red', linestyle='solid', label='4 Years Ago')
plt.axvline(biden_elected_president, color='green', linestyle='dotted', label='Joe Biden Elected')


plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('BTC-PERPETUAL Close Prices Over Time')
plt.legend()
plt.grid(True)
plt.show()