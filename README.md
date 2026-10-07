# StockAnalyzer

Python experiments for downloading historical market data, plotting financial indicators, and computing portfolio allocations. The repository also contains LangChain/OpenAI scripts for generating analysis text and code suggestions.

## Files

- `data_fetching.py`: downloads price data with yfinance.
- `kpi_data_fetching.py` and `kpi_data_in_dictionary.py`: indicator calculations and plotting.
- `finding_optimal_weights.py`: constrained Sharpe-ratio optimization with SciPy.
- `black_litterman.py`: portfolio experiments using PyPortfolioOpt.
- `OpenAI_stock_analyzer.py` and `optimized_code.py`: model-assisted analysis experiments.

## Environment

The scripts import NumPy, pandas, yfinance, matplotlib, SciPy, seaborn, PyPortfolioOpt, and langchain-openai. No pinned dependency manifest is included, so setting up a reproducible environment remains work to do.

Set `OPENAI_API_KEY` in the environment before running the scripts that call OpenAI. Keep credentials outside source control. Running those scripts can make paid API requests, including through imported modules.

## Scope

The scripts use hard-coded assets and analysis periods. Some indicator calculations combine historical prices with current company metadata, which does not establish historical EPS or P/E values. Review the formulas and data alignment before interpreting a plot. The repository does not include a validated trading strategy or a backtest demonstrating investment performance.
