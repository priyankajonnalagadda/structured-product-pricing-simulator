import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("../data/historical_prices.csv")
prices = data['Close'].tolist()

# Payoff calculations
auto_callable_payoff = [min(p / prices[0] - 1, 0.08) for p in prices[-1:]]
digital_option_payoff = [0.1 if prices[-1] > prices[0] else 0]
reverse_convertible_payoff = [min(0.05, prices[-1] / prices[0] - 1)]

# Display results
print("Auto-callable Payoff:", auto_callable_payoff)
print("Digital Option Payoff:", digital_option_payoff)
print("Reverse Convertible Payoff:", reverse_convertible_payoff)

# Plotting
plt.plot(prices)
plt.title("Underlying Price Movement")
plt.xlabel("Days")
plt.ylabel("Price")
plt.grid(True)
plt.show()

