import pandas as pd

# =========================
# PORTFOLIO DATASET
# =========================
portfolio = pd.DataFrame({
    "Stock": ["AAPL", "BP", "TSLA", "HSBC", "XOM"],
    "Sector": ["Tech", "Energy", "Auto", "Financials", "Energy"],
    "Weight": [0.25, 0.20, 0.20, 0.15, 0.20]
})

# =========================
# RETURNS DATASET
# =========================
returns = pd.DataFrame({
    "Stock": ["AAPL", "BP", "TSLA", "HSBC", "XOM"],
    "Return": [0.015, -0.01, 0.03, 0.005, 0.02]
})

# =========================
# BENCHMARK DATASET
# =========================
benchmark = pd.DataFrame({
    "Stock": ["AAPL", "BP", "TSLA", "HSBC", "XOM"],
    "Benchmark_Weight": [0.20, 0.25, 0.15, 0.20, 0.20]
})

# =========================
# DISPLAY DATA
# =========================
print("PORTFOLIO:")
print(portfolio)

print("\nRETURNS:")
print(returns)

print("\nBENCHMARK:")
print(benchmark)
