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

df = portfolio.merge(returns, on="Stock")

print("\nMERGED PORTFOLIO + RETURNS:")
print(df)

df = df.merge(benchmark, on="Stock")

print("\nAFTER ADDING BENCHMARK:")
print(df)

df["Portfolio_Contribution"] = df["Weight"] * df["Return"]

print("\nWITH CONTRIBUTION:")
print(df)

portfolio_return = df["Portfolio_Contribution"].sum()

print("\nPortfolio Return:", portfolio_return)

# =========================
# BENCHMARK CALCULATION
# =========================

df["Benchmark_Contribution"] = df["Benchmark_Weight"] * df["Return"]

benchmark_return = df["Benchmark_Contribution"].sum()

print("\nBenchmark Return:", benchmark_return)

# =========================
# ACTIVE RETURN
# =========================

active_return = portfolio_return - benchmark_return

print("Active Return:", active_return)
